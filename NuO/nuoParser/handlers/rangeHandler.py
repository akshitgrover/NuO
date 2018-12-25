import re

from .. import patterns as p
from .utils import getValue
from .. import action

RANGEOBJECT = {"isSet": False}
CURRENTRANGEOBJECT = RANGEOBJECT
RANGECOUNTER = 0

def _setRangeObject(identifier, iterValue):

    global RANGEOBJECT, CURRENTRANGEOBJECT, PREVRANGEOBJECT, RANGECOUNTER
    RANGECOUNTER += 1

    tempRangeObj = None
    if(CURRENTRANGEOBJECT["isSet"] is True):
        CURRENTRANGEOBJECT["body"].append({})
        tempRangeObj = CURRENTRANGEOBJECT
        CURRENTRANGEOBJECT = CURRENTRANGEOBJECT["body"][len(CURRENTRANGEOBJECT["body"]) - 1]

    CURRENTRANGEOBJECT["prev"] = tempRangeObj
    CURRENTRANGEOBJECT["iterValue"] = iterValue
    CURRENTRANGEOBJECT["id"] = identifier
    CURRENTRANGEOBJECT["body"] = []
    CURRENTRANGEOBJECT["isSet"] = True

def startRangeBlock(expression):

    for elem in p._range.finditer(expression):
        x, y = list(elem.span())
        tempExp = expression[x + 1:y - 1].strip().split()

        identifier, iterKey = list(tempExp[1].split(":"))

        _setRangeObject(identifier, iterKey)

def putLine(expression):
    global CURRENTRANGEOBJECT
    CURRENTRANGEOBJECT["body"].append(expression)

def endRangeBlock():
    global RANGEOBJECT, CURRENTRANGEOBJECT, RANGECOUNTER

    if(RANGECOUNTER is not 1):
        CURRENTRANGEOBJECT = CURRENTRANGEOBJECT["prev"]
        action.setAction("range")
        RANGECOUNTER -= 1
        return

    action.setAction("file")
    RANGETEMPDATA = {}
    RANGECOUNTER -= 1

    def parseRangeExp(id, line):

        if(re.compile("{[a-zA-Z0-9_\-\.]+}").search(line) is not None):
            modExpression = []
            z = 0

            for elem in re.compile("{[a-zA-Z0-9_\-\.]+}").finditer(line):

                x, y = list(elem.span())
                tempExp = line[x + 1:y - 1].strip().split(".")
                modExpression.append(line[z:x])

                _v = getValue(tempExp, True, RANGETEMPDATA)
                modExpression.append(str(_v))

                z = y

            modExpression.append(line[z:])
            return "".join(modExpression)
        else:
            return line

    def _parseRangeBody(id, rb):
        for i in rb:
            if(type(i) is dict):
                parseRange(i)
            else:
                i = i.strip()
                action.takeAction(parseRangeExp(id, i))

    def parseRange(rangeObj):

        if(type(rangeObj["iterValue"]) is str and rangeObj["iterValue"].isdigit()):
            rangeObj["iterValue"] = int(rangeObj["iterValue"])
        elif(type(rangeObj["iterValue"]) is str):
            iterKey = rangeObj["iterValue"].split(".")
            rangeObj["iterValue"] = getValue(iterKey, True, RANGETEMPDATA)

        t = type(rangeObj["iterValue"])
        Iter = _getIter(t, rangeObj["iterValue"])
        if(t is not dict):
            for i in Iter:
                RANGETEMPDATA[rangeObj["id"]] = i
                _parseRangeBody(rangeObj["id"], rangeObj["body"])
        else:
            RANGETEMPDATA[rangeObj["id"]] = {}
            for k, v in Iter.items():
                RANGETEMPDATA[rangeObj["id"]]["k"] = k
                RANGETEMPDATA[rangeObj["id"]]["v"] = v
                _parseRangeBody(rangeObj["id"], rangeObj["body"])

    parseRange(RANGEOBJECT)
    RANGEOBJECT = {"isSet": False}
    RANGECOUNTER = 0
    CURRENTRANGEOBJECT = RANGEOBJECT

def _getIter(t, val):

    if(t is int):
        return range(val)
    else:
        return val

import re

import siteData as sd
from .. import patterns as p
from .utils import chainedPropertyAccess
from .. import action

RANGEOBJECT = {"isSet": False}

def _setRangeObject(identifier, iterValue):

    global RANGEOBJECT
    RANGEOBJECT = {}
    RANGEOBJECT["iterValue"] = iterValue
    RANGEOBJECT["id"] = identifier
    RANGEOBJECT["body"] = []
    RANGEOBJECT["isSet"] = True

def startRangeBlock(expression):

    for elem in p._range.finditer(expression):
        x, y = list(elem.span())
        tempExp = expression[x + 1:y - 1].strip().split()

        identifier, iterKey = list(tempExp[1].split(":"))
        iterKey = iterKey.split(".")

        if(len(iterKey) == 1):
            root = iterKey[0]
        
        if(root.isdigit()):
            iterValue = int(root)
        elif(root in sd.GLOBALS.keys()):
            if(len(iterKey) == 1):
                iterValue = sd.GLOBALS[root]
            else:
                iterValue = chainedPropertyAccess(sd.GLOBALS[root], iterKey[1:])
        
        _setRangeObject(identifier, iterValue)

def putLine(expression):
    global RANGEOBJECT
    RANGEOBJECT["body"].append(expression)

def endRangeBlock():
    
    action.setAction("file")
    RANGETEMPDATA = {}

    def parseRangeExp(id, line):

        if(re.compile("{[a-zA-Z_\-\.]}").search(line) is not None):
            modExpression = []
            z = 0

            for elem in re.compile("{[a-zA-Z_\-\.]+}").finditer(line):
                
                x, y = list(elem.span())
                tempExp = line[x + 1:y - 1].split(".")
                modExpression.append(line[z:x])
                
                if(len(tempExp) == 1):
                    modExpression.append(str(RANGETEMPDATA[id]))
                elif(tempExp[1] == "key"):
                    modExpression.append(RANGETEMPDATA[id]["key"])
                elif(tempExp[1] == "value"):
                    modExpression.append(RANGETEMPDATA[id]["value"])
                z = y

            return "".join(modExpression)
        else:
            return line

    def parseRange(rangeObj):

        if(type(rangeObj["iterValue"]) is int):
            for i in range(rangeObj["iterValue"]):
                RANGETEMPDATA[rangeObj["id"]] = i
                for j in rangeObj["body"]:
                    j = j.strip()
                    action.takeAction(parseRangeExp(rangeObj["id"], j))
        else:
            RANGETEMPDATA[rangeObj["id"]] = rangeObj["iterValue"]

    parseRange(RANGEOBJECT)

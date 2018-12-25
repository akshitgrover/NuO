import os
import re

from NuO.siteData import *
from . import patterns as p
from .action import setAction, takeAction, openFile, closeFile
from .handlers import var, define, rangeHandler, arithmetic as a

def start():
    files = os.listdir(NUODIR)
    parse(files = files)

def parse(files = [], prefix = NUODIR):
    pattern = re.compile("^.*\.nuo$")
    for file in files:
        file = os.path.join(prefix, file)
        if(os.path.isdir(file)):
            os.mkdir("build/" + file[len(NUODIR):])
            parse(os.listdir(file), file)
        if pattern.match(file) is not None:
            parseFile(file)
            pass
        else:
            pass

def parseFile(file):
    if os.path.exists(file):
        baseName = file[len(NUODIR):]
        outputFileName = "build/" + baseName.split(".")[0] + ".html"
        openFile(outputFileName)

        f = open(file, "r")
        for line in f.readlines():
            method = detectPattern(line)

            if method == "var":
                line = var.exp(line)
                takeAction(line)

            if method == "define":
                define.exp(line)

            if method == "range":
                setAction("range")
                rangeHandler.startRangeBlock(line)

            if method == "rangeEnd":
                setAction("rangeEnd")
                takeAction(line)

            if method == "arithmetic":
                line = a.eval(line)
                takeAction(line)

            if method == "raw":
                takeAction(line)

        closeFile()

    else:
        raise Exception("File '{}' does not exist".format(file))

def detectPattern(expression):
    if p._var.search(expression) is not None:
        return "var"

    if p._range.search(expression) is not None:
        return "range"

    if p._define.search(expression) is not None:
        return "define"

    if p._rangeEnd.search(expression) is not None:
        return "rangeEnd"

    if p._arithmetic.search(expression) is not None:
        return "arithmetic"

    return "raw"

import os
import re

from siteData import *
from . import patterns as p
from .action import setAction, takeAction, openFile, closeFile
from .handlers import var
from .handlers import define

def start():
    files = os.listdir(NUODIR)
    parse(files = files)

def parse(files = []):
    pattern = re.compile("^.*\.nuo$")
    for file in files:
        if pattern.match(file) is not None:
            parseFile(file)
        else:
            pass

def parseFile(file):
    file = os.path.join(NUODIR, file)
    if os.path.exists(file):
        
        outputFileName = "build/" + os.path.basename(file).split(".")[0] + ".html"
        openFile(outputFileName)

        f = open(file, "r")
        for line in f.readlines():
            method = detectPattern(line)
            if method == "var":
                line = var.exp(line)
                takeAction(line, file)
                # print(line)
            if method == "define":
                define.exp(line)
                pass
                # print(DEFINEDOBJECTS)
            if method == "range":
                print("range")
        
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
import os

__all__ = ["GLOBALS", "NUODIR", "DATAFILESOBJECT", "DATAOBJECT", "DEFINEDOBJECTS", "setNuoDir", "siteData"]

GLOBALS = {}

NUODIR = os.getcwd()

DATAFILESOBJECT = {}

DATAOBJECT = {}

DEFINEDOBJECTS = {}  #Objects defined during parser runtime with "define" directive

def setNuoDir(nuoDir):
    global NUODIR
    NUODIR = nuoDir

def siteData(verbose = False):
    if(verbose):
        print("Globals: {}".format(GLOBALS), end = "\n\n")
        print("NuoFiles Directory: {}".format(NUODIR), end = "\n\n")
        print("Data Files: {}".format(DATAFILESOBJECT), end = "\n\n")

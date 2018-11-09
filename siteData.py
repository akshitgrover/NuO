import os

__all__ = ["GLOBALS", "NUODIR", "DATAFILESOBJECT", "DATAOBJECT", "setNuoDir", "siteData"]

GLOBALS = {}

NUODIR = os.getcwd()

DATAFILESOBJECT = {}

DATAOBJECT = {}

def setNuoDir(nuoDir):
    NUODIR = nuoDir

def siteData(verbose = False):
    if(verbose):
        print("Globals: {}".format(GLOBALS), end = "\n\n")
        print("NuoFiles Directory: {}".format(NUODIR), end = "\n\n")
        print("Data Files: {}".format(DATAFILESOBJECT), end = "\n\n")
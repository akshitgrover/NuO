import os

__all__ = ["GLOBALS", "NUODIR", "DATAFILESOBJECT", "DATAOBJECT"]

GLOBALS = {}

NUODIR = os.getcwd()

DATAFILESOBJECT = {}

DATAOBJECT = {}

def setNuoDir(nuoDir):
    NUODIR = nuoDir
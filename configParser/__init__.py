import os

__all__ = ["parser", "DATAOBJECT", "GLOBALS", "NUODIR", "DATAFILES"]

DATAOBJECT = {}
GLOBALS = {}

NUODIR = os.getcwd()
DATAFILES = []

def setNuoDir(directory):
    NUODIR = directory
import os
import json

import yaml

import siteData as sd
import dataInterface as di

def parse(configFilePath):

    if(not os.path.isabs(configFilePath)):
        currentDir = os.getcwd()
        configFilePath = os.path.join(currentDir, configFilePath)

    configFile = open(configFilePath, "r")
    configContent = configFile.read()
    parsedContent = yaml.load(configContent)
    _placeData(parsedContent)

def _placeData(data):

    sd.GLOBALS.update(data["globals"])
    sd.DATAFILESOBJECT.update(data["datafiles"])
    
    sd.setNuoDir(data["nuodir"])

    di.placeData()
    
import os
import json

import yaml

import configParser as cp

def parse(configFilePath):

    if(not os.path.isabs(configFilePath)):
        currentDir = os.getcwd()
        configFilePath = os.path.join(currentDir, configFilePath)

    configFile = open(configFilePath, "r")
    configContent = configFile.read()
    parsedContent = yaml.load(configContent)
    _placeData(parsedContent)

def _placeData(data):

    cp.GLOBALS.update(data["globals"])
    cp.setNuoDir(data["nuodir"])
    currentDir = os.getcwd()
    
    dataFiles = data["datafiles"]

    for dkey in data["datafiles"].keys():
        if(not os.path.isabs(dataFiles[dkey])):
            dataFiles[dkey] = os.path.join(currentDir, dataFiles[dkey])
        cp.DATAFILES.append(dataFiles[dkey])

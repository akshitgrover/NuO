import os

import yaml

import NuO.siteData as sd
import NuO.dataInterface as di

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

    sd.setNuoDir(os.path.abspath(data["nuodir"]))

    di.placeData()

import os
import json

import NuO.siteData as sd

def placeData():

    for key in sd.DATAFILESOBJECT.keys():
        value = sd.DATAFILESOBJECT[key]
        value = os.path.abspath(value)

        dataFile = open(value, "r")
        data = dataFile.read()
        parsedJsonData = json.loads(data)

        sd.DATAOBJECT[key] = parsedJsonData

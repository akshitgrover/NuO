import os

from .handlers import rangeHandler

_openedFile = None

ACTION = "file"

HTML_DIRECTORY = os.path.abspath("build")

"""Set to hold actions defined in nuoParser
Description of actions

"file": To write a line to build file"""
actionSet = {"file", "range", "rangeEnd"}

#Function ot set current action for nuoParser
def setAction(action):

    #Refer to ACTION variable outside function scope
    global ACTION

    #Check if action is present is actionSet
    if(action not in actionSet):
        raise Exception("Action '{}' is not defined".format(action))

    #Set ACTION to specified action
    ACTION = action

#Function to open output html file in "build/" folder by default
def openFile(file):

    #Refer to _openedFile variable outside function scope
    global _openedFile
    _openedFile = open(file, "+a")

#Function to close output html file referd by _openedFile global variable
def closeFile():

    #Refer to _openedFile varaible outside function scope
    global _openedFile
    _openedFile.close()  #Close file
    _openedFile = None  #Switch to None object

#Function to execute current action for the nuoParser
def takeAction(line):

    #Check if current action is file
    if(ACTION == "file"):

        #Refer to _openedFile outside function scope
        global _openedFile

        #Check if a file is opened
        if(_openedFile is None):
            raise Exception("HTML Output: No file is opened to write")

        #Initiate write procedure
        _openedFile.write(line.strip() + "\r\n")

    if(ACTION == "range"):

        rangeHandler.putLine(line)

    if(ACTION == "rangeEnd"):

        rangeHandler.endRangeBlock()

import siteData as sd
from .. import patterns as p
from .utils import chainedPropertyAccess

#Function to define variables as parsed from nuo files
def exp(expression):

    #Iterate over matched regexp expressions
    for elem in p._define.finditer(expression):
        x, y = list(elem.span())

        #Variable that holds expression within curly bounds
        tempExp = expression[x + 2: y - 2].strip().split()

        #identifier of the value to be assigned, Referring to an already assigned object
        refObj = tempExp[2].split(".")
        root = refObj[0]

        #Check for the existence of object in glboal variables
        if(root in sd.GLOBALS.keys()):

            #Check if there is no property chaining
            if(len(refObj) == 1):
                val = sd.GLOBALS[root]
            else:
                val = chainedPropertyAccess(sd.GLOBALS[root], refObj[1:])

        #Check for the existence of object in in data files
        elif(root in sd.DATAOBJECT.keys()):

            #Check is there is no property chaining
            if(len(refObj) == 1):
                val = sd.DATAOBJECT[root]
            else:
                val = chainedPropertyAccess(sd.DATAOBJECT[root], refObj[1:])

        #Check for the existence of object in earlier defined objects
        elif(root in sd.DEFINEDOBJECTS.keys()):

            #Check is there is no property chaining
            if(len(refObj) == 1):
                val = sd.DEFINEDOBJECTS[root]
            else:
                val = chainedPropertyAccess(sd.DEFINEDOBJECTS[root], refObj[1:])

        #Set the value of key as per expression in nuo file
        sd.DEFINEDOBJECTS[tempExp[1]] = val

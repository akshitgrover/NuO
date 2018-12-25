import NuO.siteData as sd
from .. import patterns as p
from .utils import chainedPropertyAccess

#Function to parse variables in a string expression
def exp(expression):

    #List to store parsed terms as per input string (expression)
    modExpression = []

    #Variable to define offest for next term in resultant string
    z = 0

    for elem in p._var.finditer(expression):
        x, y = elem.span()
        tempVar = expression[x + 2:y - 2].strip().split(".")

        modExpression.append(expression[z:x])

        #Check for globals
        if(len(tempVar) == 1 and tempVar[0] in sd.GLOBALS.keys()):
            modExpression.append(str(sd.GLOBALS[tempVar[0]]))

        #Check for objects in data files
        elif(len(tempVar) == 1 and tempVar[0] in sd.DATAOBJECT.keys()):
            modExpression.append(str(sd.DATAOBJECT[tempVar[0]]))

        #Check for objects in defined objeccts
        elif(len(tempVar) == 1 and tempVar[0] in sd.DEFINEDOBJECTS.keys()):
            modExpression.append(str(sd.DEFINEDOBJECTS[tempVar[0]]))

        #Check for object properties
        elif(len(tempVar) > 1):
            root = tempVar[0]

            #Check for object properties in globals
            if(root in sd.GLOBALS.keys()):
                value = chainedPropertyAccess(sd.GLOBALS[root], tempVar[1:])
                modExpression.append(str(value))

            #Check for object properties in data files
            elif(root in sd.DATAOBJECT.keys()):
                value = chainedPropertyAccess(sd.DATAOBJECT[root], tempVar[1:])
                modExpression.append(str(value))

            #Check for object properties in earlier defined objects
            elif(root in sd.DEFINEDOBJECTS.keys()):
                value = chainedPropertyAccess(sd.DEFINEDOBJECTS[root], tempVar[1:])
                modExpression.append(str(value))

        #Store offset value for next term in resultant string
        z = y

    #Append trailing term in input expression
    modExpression.append(expression[z:])

    #Return parsed string
    return "".join(modExpression).strip()

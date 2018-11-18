#Function to access properties of object
def chainedPropertyAccess(obj, arr = []):

    #Check for unit case
    if(len(arr) == 1):
        try:
            #Unit case, Return Value of chained properties of an object
            return obj[arr[0]]
        except KeyError:
            #Return empty string when interrupt is a KeyError
            return ""
    else:
        #Handle KeyError
        try:
            #Recursive to call access property of property of an object
            return chainedPropertyAccess(obj[arr[0]], arr[1:])
        except KeyError:
            #Return empty string when interrupt is a KeyError
            return ""
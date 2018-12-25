import NuO.siteData as sd
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[len(self.stack) - 1]

    def isEmpty(self):
        return True if (len(self.stack) == 0) else False

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

def getPostfix(exp):

    postfix = ""
    operators = ["+", "-", "/", "*"]
    pre = {"+": 1, "-": 1, "*": 2, "/": 2}
    stack = Stack()

    for char in exp:
        if(char == '('):
            stack.push(char)
            continue

        if(char not in operators and char is not "(" and char is not ")"):
            postfix += char
            continue

        if(char == ")"):
            while(stack.top() is not "("):
                postfix += " " + stack.pop() + " "
            stack.pop()
            continue

        if(stack.isEmpty() or stack.top() == "(" or pre[stack.top()] < pre[char]):
            stack.push(char)
            continue
        else:
            while(1):
                if(stack.isEmpty() or stack.top() == "(" or pre[stack.top()] < pre[char]):
                    break
                postfix += " " + stack.pop() + " "
            stack.push(char)

    while(not stack.isEmpty()):
        postfix += " " + stack.pop() + " "

    return postfix

def evalPostfix(expression):

    tempExp = expression.split()
    operators = ["+", "-", "/", "*"]
    stack = Stack()

    for op in tempExp:
        if(op in operators):
            x, y = stack.pop(), stack.pop()
            if(type(x) is int or x.isdigit()):
                stack.push(_eval(int(x), int(y), op))
            else:
                x = getValue(x)
                stack.push(_eval(x, y, op))
            continue
        if(op is not " "):
            stack.push(op)

    return stack.top()

def _eval(x, y, op):

    if(op == "+"):
        return y + x

    if(op == "-"):
        return y - x

    if(op == "/"):
        return int(y / x)

    if(op == "*"):
        return y * x

def getValue(ch, rangeData = False, rangeDataObj = {}):

    if(rangeData and ch[0] in rangeDataObj.keys()):
        return chainedPropertyAccess(rangeDataObj, ch)

    if(ch[0] in sd.GLOBALS.keys()):
        return chainedPropertyAccess(sd.GLOBALS, ch)

    if(ch[0] in sd.DATAOBJECT.keys()):
        return chainedPropertyAccess(sd.DATAOBJECT, ch)

    if(ch[0] in sd.DEFINEDOBJECTS.keys()):
        return chainedPropertyAccess(sd.DEFINEDOBJECTS, ch)

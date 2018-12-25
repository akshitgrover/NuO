from .. import patterns as p
from .utils import getPostfix, evalPostfix, getValue

def eval(expression):

	operators = ["+", "-", "/", "*"]
	modExpression = []
	z = 0
	for elem in p._arithmetic.finditer(expression):

		x, y = elem.span()
		tempExp = expression[x + 2:y - 2]
		modExpression.append(expression[z:x])

		pFix = getPostfix(tempExp)
		pFix = pFix.split(" ")
		for i in range(len(pFix)):

			ch = pFix[i]
			if(not ch.isdigit() and ch is not "" and ch not in operators):
				ch = ch.split(".")
				pFix[i] = str(getValue(ch))
		modExpression.append(str(evalPostfix(" ".join(pFix))))
		z = y
	modExpression.append(expression[z:])
	return "".join(modExpression)

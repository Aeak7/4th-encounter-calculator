from functions import *

# import variables: fileName.variableName (functions.inputVariable)


# checkOrder(insideOrderInput, allowedInsideOrder)
# checkOrder(outsideOrderInput, possibleOutsideShapes) # test this

# insideLetterList = spliceString(insideOrderInput)
# outsideLetterList = spliceString(outsideOrderInput)

allowedInsideOrder = ['cst', 'cts', 'stc', 'sct', 'tsc', 'tcs']
# both inside and outside orders are from left to right and with the first letter of the shape
# Ex: circle = c, square = s, triangle = t

# allowedOutsideOrder = ['st', 'ts', 'cs', 'sc', 'tt', 'ct', 'ss', 'tc', 'cc']
# outside orders are based on a combination of the 2 shapes the shape is made of
# Ex: sphere = cc
# this does account for reversals
# | prism = st, ts | pyramid = tt | cylinder = sc, cs | cone = ts, st | cube = ss | sphere = cc |
allowedOutsideShapes = ['prism', 'pyramid', 'cylinder', 'cone', 'cube', 'sphere'] # i mean this technically becomes the allowedOrder?


print('Your inside order is: ' + getInsideOrder())
# OUTSIDE ORDER NEEDS 3 SHAPES, NOT JUST ONE SHAPE ^^
print('Your outside order is: ' + getOutsideOrder())
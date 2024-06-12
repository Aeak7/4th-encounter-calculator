allowedInsideOrder = ['cst', 'cts', 'stc', 'sct', 'tsc', 'tcs']
# both inside and outside orders are from left to right and with the first letter of the shape
# Ex: circle = c, square = s, triangle = t

# allowedOutsideOrder = ['st', 'ts', 'cs', 'sc', 'tt', 'ct', 'ss', 'tc', 'cc']
# outside orders are based on a combination of the 2 shapes the shape is made of
# Ex: sphere = cc
# this does account for reversals
# | prism = st, ts | pyramid = tt | cylinder = sc, cs | cone = ts, st | cube = ss | sphere = cc |
possibleOutsideShapes = ['prism', 'pyramid', 'cylinder', 'cone', 'cube', 'sphere'] # i mean this technically becomes the allowedOrder?

# OUTSIDE ORDER NEEDS 3 SHAPES, NOT JUST ONE SHAPE ^^
outsideOrderInput = str(input('Please enter the outside order (FORMAT: left, middle, right): ').lower().split(','))
print('Your outside order is: ' + outsideOrderInput)

# def checkOutsideOrder(order, allowedOrder, shapesList):
#   if order in shapesList:
#     print()

insideOrderInput = str(input('Please enter the inside order (ex: cst): ').lower())
print('Your inside order is: ' + insideOrderInput)
# outsideOrderInput = str(input('Please enter the outside order: (ex: ss) ').lower())
# print('Your outside order is: ' + outsideOrderInput)


def checkOrder(order, allowedOrder):
  if order in allowedOrder:
    print('ACCEPTED STRING')
    return order
  else:
    print('INCORRECT STRING')
    order = str(input('Re-enter a new order or type 7 to cancel: ').lower())
    if order == '7':
      return
    else:
      checkOrder(order)

def spliceString(orderString):
  separatedLetterList = []
  for letter in orderString:
    separatedLetterList.append(letter)
  return separatedLetterList

def assignPositions(letterList):
  letterPositions = dict(left = letterList[0], middle = letterList[1], right = letterList[2])
  return letterPositions



# checkOrder(insideOrderInput, allowedInsideOrder)
# checkOrder(outsideOrderInput, possibleOutsideShapes) # test this

# insideLetterList = spliceString(insideOrderInput)
# outsideLetterList = spliceString(outsideOrderInput)




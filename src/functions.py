def getOutsideOrder():
  outsideOrderInput = str(input('Please enter the outside order (FORMAT: left, middle, right): ').lower().split(','))
  return outsideOrderInput

def getInsideOrder():
  insideOrderInput = str(input('Please enter the inside order (ex: cst): ').lower())
  return insideOrderInput

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

# def checkOutsideOrder(order, allowedOrder, shapesList):
#   if order in shapesList:
#     print()
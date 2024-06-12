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

# 
def spliceString(orderString):
  separatedLetterList = []
  for letter in orderString:
    separatedLetterList.append(letter)
  return separatedLetterList

# assigns inside positions (cst) to left, middle, or right 
# def assignPositions(letterList):
#   letterPositions = dict(left = letterList[0], middle = letterList[1], right = letterList[2])
#   return letterPositions

# assigns inside letters (cst) with outside 3d shapes
def assignPairs(letterList, outsideOrderInput):
  leftLetter = letterList[0]
  middleLetter = letterList[1]
  rightLetter = letterList[2]
  positionPairs = dict(leftLetter = outsideOrderInput[0], middleLetter = outsideOrderInput[1], rightLetter = outsideOrderInput[2])
  return positionPairs

def findCorrectSolution(positionPairs):
  keys = positionPairs.keys()
  for key in keys:
    if key == 'c':
      positionPairs.update({'c' : 'ts'})
    if key == 't':
      positionPairs.update({'t' : 'sc'})
    if key == 's':
      positionPairs.update({'s' : 'tc'})
  return positionPairs
    
def checkMatchingPerPillar(positionPairs):
  for key in positionPairs:
    if key == positionPairs[key]:
      isPillarGood = False

# if triangle left:
#   if has triangle in it = bad
#   if has sphere or cube = bad
    
      




# def checkOutsideOrder(order, allowedOrder, shapesList):
#   if order in shapesList:
#     print()
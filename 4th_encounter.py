print('Enter the inside order:')
insideOrder = input().lower()
print('You typed in:' + insideOrder)
allowedInsideOrder = ['cst', 'cts', 'stc', 'sct', 'tsc', 'tcs']
for items in allowedInsideOrder:
  if items != insideOrder:
    print('This is not a correct order')
    insideOrder = input().lower()
  else:
    print('Your input is correct!')
def checkPattern(ptr):
  
  stack = []
  
  pair = {
    ']' : '[',
    '}' : '{',
    ')' : '('
  }
  
  for p in ptr:
    if p in pair:
      if not stack or stack[-1] != pair[p]:
              return False
      else:      
        stack.pop()
    else:
      stack.append(p)
  return len(stack) == 0

strr = '[{()}]'
ptr = '(){}[]'
ptr1 = '{[}]'

print(checkPattern(strr))
print(checkPattern(ptr))
print(checkPattern(ptr1))
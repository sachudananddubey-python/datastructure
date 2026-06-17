#check pattern [{()}] ,{[}]

def pattern(lst):
  stack = []
  dist ={
    ')' : '(',
    '}' : '{',
    ']' : '['
  }
  for i in lst:
    if i in dist:
      if stack[-1] == dist[i]:
        stack.pop()     
    else:
      stack.append(i)
  return len(stack)==0
    

print(pattern("[{()}]"))  # True
print(pattern("{[}]"))    # False
print(pattern("[{(}])"))  # False
  


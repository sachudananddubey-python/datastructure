class Stack:
  
  def __init__(self,pattern):
    self.pattern = pattern
  
  def is_valid(self):
    pattern = self.pattern
    stack = []
    dic = {
      '}' : '{',
      ']' : '[',
      ')' : '(' 
    }
    
    for p in pattern:
      if p in dic:
        if stack and stack[-1] == dic[p]:
          stack.pop()
        else:
          return False
      else:
        stack.append(p)
    return len(stack) == 0
  
pattern = '{()}'
s = Stack(pattern)
print(s.is_valid())
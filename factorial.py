def fact(n):
  if n <= 1:
    return 1
  else:
    while n > 1:
      return n * fact(n-1)
    
n = 6
print(fact(n))
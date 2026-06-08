def lowerTriangle(n):
  for i in range(n):
    
    print(" "*(n-i),end="")
    
    print("* "*i)
    
  for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    
    print("* "*i)
  
lowerTriangle(5)
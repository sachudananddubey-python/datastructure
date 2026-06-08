def Row(n):
  for i in range(n):
    for j in range(i):
      print("*",end="")
    print()

Row(5)
  
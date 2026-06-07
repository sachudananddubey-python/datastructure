stack = []

stack.append("A")
stack.append("B")
stack.append("C")
stack.append("D")

#peek
lastElement = stack[-1]
print(lastElement)

#get and remove last element
removeElement = stack.pop()
print(removeElement)
print(stack)


#check empty stack
isEmpty = not bool(stack)
print(isEmpty)

#size
size = len(stack)
print(size)
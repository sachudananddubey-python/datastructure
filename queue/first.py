queue = []

queue.append("A")
queue.append("B")
queue.append("C")
queue.append("D")

#peek
frontElement = queue[0]
print(frontElement)

#remove and get first element
poppedElement = queue.pop(0)
print(poppedElement)

#empty queue
isEmpty = not bool(queue)
print(isEmpty)

#size
size = len(queue)
print(size)



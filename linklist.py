class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class linkList:
  
  def __init__(self):
    self.head = None
  
  def insert(self,data):
    new_node = Node(data)
    
    if self.head is None:
      self.head = new_node
      return
    
    temp = self.head
    while temp.next:
      temp = temp.next
    temp.next = new_node
    
  def display(self):
    temp = self.head
    
    while temp:
      print(temp.data , end=" -> ")
      temp = temp.next
    print("None")  
  
  def remove(self,data):
    temp = self.head
    pre = None
    
    if temp.data == data:
      self.head = None
      return
    
    while temp:
      if temp.data == data:
        break
      pre = temp
      temp = temp.next
    pre.next = temp.next
    temp = None
    
link = linkList()
link.insert(12)
link.insert(13)
link.insert(20)
link.insert(50)
link.display()
link.remove(20)
link.display()
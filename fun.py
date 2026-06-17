class Node:
  def __init__(self,data):
    self.data = data 
    self.next = None
    

class Linklist:
  
  def __init__(self):
    self.head = None
  
  def insert(self,data):
    
    new_node = Node(data)
    temp = self.head
    
    if temp is None:
      self.head = new_node
      return
    
    while temp.next:
      temp = temp.next
      
    temp.next = new_node
    
  def display(self):
    temp = self.head
    
    if self.head is None:
      print("OOPSss... No data assign")
    
    while temp:
      print(temp.data , end=" -> ")
      temp = temp.next
    print("None")
      
link = Linklist()

link.insert(10)
link.insert(50)
link.insert(30)
link.insert(40)
link.insert(20)
link.insert(5)
link.display()

link1=Linklist()
link1.insert(2)
link1.insert(3)
link1.display()



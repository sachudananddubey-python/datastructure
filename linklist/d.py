class Node:
  def __init__(self,data):
    self.prev = None
    self.data = data
    self.next = None
    
class linkList:
  
  def __init__(self):
    self.head = None
  
  def insert(self,data):
    
    temp = self.head
    new_node = Node(data)
    
    if temp is None:
      self.head = new_node
      return
      
    while temp.next:
      temp = temp.next
    
    temp.next = new_node
    new_node.prev = temp
  
  def dispay_forward(self):
    temp = self.head
   
    if temp.next is None:
      print(temp.data)
      return 
    
    while temp:
      print(temp.data,end=" <=> ")
      temp = temp.next
      
    print("None")
    
  def dispay_backword(self):
    temp = self.head
    
    if temp.next is None:
      print(temp.data)
      return
    
    while temp.next:
      temp = temp.next
    
    while temp:
      print(temp.data,end=" <=> ")
      temp = temp.prev
    print("None")  


link = linkList()
link.insert(10)
link.insert(20)
link.insert(30)
link.insert(40)
link.insert(50)
link.insert(60)
link.dispay_forward()
link.dispay_backword()
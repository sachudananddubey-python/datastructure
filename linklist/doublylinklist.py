class Node:
  def __init__(self,data):
    self.data = data
    self.prev = None
    self.next = None
  
class Doublylink:
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
    new_node.prev = temp 
  
  def display_forward(self):
    
    temp = self.head
    
    if temp.next is None:
      
      print(temp.data)
      
      return
    
    while temp:
      
      print(temp.data,end=" <-> ")
      
      temp = temp.next
    print("None")
    
  def display_backword(self):
    
    temp = self.head
    
    while temp.next:
      temp = temp.next
      
    while temp:
      print(temp.data,end=" <-> ")
      temp = temp.prev
    print("None")
    
    
def delete(self, data):
  
    temp = self.head

    while temp:
        if temp.data == data:
            break
        temp = temp.next

    # data not found
    if temp is None:
        return

    # Head node delete
    if temp == self.head:
        self.head = temp.next

        if self.head:
            self.head.prev = None

        return

    # Last ya middle node delete
    if temp.prev:
        temp.prev.next = temp.next

    if temp.next:
        temp.next.prev = temp.prev
      
    
link = Doublylink()
link.insert(10)
link.insert(20)
link.insert(30)
link.insert(40)
link.insert(50)
link.insert(60)
link.display_forward()
link.delete(50)
link.display_forward()
# link.display_backword()
    
      
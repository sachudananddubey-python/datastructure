class Node:
  
  def __init__(self,data):
    self.data = data
    self.next = None
    self.prev = None

class linkList:
  
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
    
  def remove(self,data):
    temp = self.head
    pre = None
    if temp.next is None:
      temp = None
      return
    
    while temp:
      if temp.datdef remove(self, data):
      temp = self.head

    if temp is None:
        return

    # agar head delete karna ho
    if temp.data == data:
        self.head = temp.next

        if self.head:
            self.head.prev = None

        return

    # data search karo
    while temp:
        if temp.data == data:
            break
        temp = temp.next

    # data nahi mila
    if temp is None:
        return

    # middle ya last node delete
    if temp.next:
        temp.next.prev = temp.prev

    if temp.prev:
        temp.prev.next = temp.next

link = linkList()
link.insert(10)
link.insert(20)
link.insert(30)
link.insert(40)
link.insert(50)
link.insert(60)  
link.insert(70)
link.display_forward()
link.display_backword()
link.remove(60)
link.display_forward()
link.display_backword()
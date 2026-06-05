class Index:
  
  def __init__(self,lst):
    self.lst = lst
  
  def getIndex(self):
    lst = self.lst
    
    new_lst = []
    for i in range(len(lst)):
      rank = 1
      for j in range(len(lst)):
        if lst[i] > lst[j]:
          rank += 1
      new_lst.append(rank)
    return new_lst

lst = [50,20,60,10,5,35]
i = Index(lst)
print(i.getIndex())
    
  
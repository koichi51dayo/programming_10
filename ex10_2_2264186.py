import copy
class Item:
    def __init__(self, name:str, weight:int):
        self.name = name
        self.weight = weight
        
items=[Item("A",7),Item("B",6),Item("C",5),Item("D",4),Item("E",3)]
N = len(items)    
sel = [False]*N   
ans=[]
limw=15

def try_item(i,tw):
  global sel,ans
  if tw+items[i].weight<=limw:
    sel[i]=True
    if i<N-1:
      try_item(i+1,tw+items[i].weight)
    elif tw+items[i].weight==limw:
      ans.append(copy.deepcopy(sel))
    sel[i] = False 
    
  if i<N-1:
    try_item(i+1,tw)
  elif tw==limw:
    ans.append(copy.deepcopy(sel)) 
    
try_item(0,0)
sels=[]
print("最大積載量 15t の荷物の組み合わせは")
for optsel in ans:
  for it,s in zip(items,optsel):
    if s:
      stritem=it.name+":"+str(it.weight)+"t"
      sels.append(stritem)
  ansstr=" + ".join(sels)
  print(ansstr)
  sels=[]

        
    
  
    
    
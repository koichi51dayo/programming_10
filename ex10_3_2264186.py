import copy
data=[
    [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
    [8,8,8,8,8,1,5,5,5,5,5,5,5,4,8],
    [8,8,8,8,5,5,5,8,8,8,8,8,5,8,8],
    [8,8,8,5,8,5,8,5,8,8,8,5,8,8,8],
    [8,8,5,8,8,5,8,8,5,8,5,8,8,8,8],
    [8,0,5,5,5,2,5,5,5,3,8,8,8,8,8],
    [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]
]
number=0
ans=[0]

def tansaku(i:int,x:int,y:int):
    global data,number,ans
    move_vec=[(1,0),(1,-1),(1,1),(0,1),(0,-1),(-1,-1)]
    
    for dx,dy in move_vec:
        x1=x+dx
        y1=y+dy
        
        if data[y1][x1]==5:
            while data[y1][x1]==5:
                move_to(x1,y1)
                x1+=dx
                y1+=dy
            if data[y1][x1]==4:
                ans.append(4)
                number+=1
                print("解番号 {:d},手数{:d}".format(number,i+1))
                keep=copy.deepcopy(data)
                henkan(keep)
                print(ans)
                ans.remove(4)
                
            
            elif not data[y1][x1] in ans:
                ans.append(data[y1][x1])
                tansaku(i+1,x1,y1)
                
            while data[y1-dy][x1-dx]==6:
                undo(x1-dx,y1-dy)
                x1-=dx
                y1-=dy
    ans.remove(data[y1-dy][x1-dx])
                
            
            
        
            
def undo(x:int, y:int):
    global data   
    data[y][x]=5
        
def move_to(x:int,y:int):
    global data
    data[y][x]=6
    
def henkan(data:list):
  copy=data
  for i in range(7):
      for j in range(15):
          copy[i][j]=str(data[i][j])
  Marks={0:"🔴",1:"🔴",2:"🔴",3:"🔴",4:"🟡",5:"⬜️",6:"🔵",8:"⬛"}
  for i in range((len(copy))):
      for idx,x in enumerate(data[i]):
          if int(x) in Marks:
              copy[i][idx]=data[i][idx].replace(x,Marks[int(x)])
  for i in range(7):
      copy[i]=''.join(copy[i])
      print(copy[i])
      
tansaku(0,1,5)
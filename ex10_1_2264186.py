x=0
move_vec=list(range(1,10))

def tansaku():
    global move_vec
    global x
    for dy in move_vec:      
        move_to(dy)
        if x<10**3:
          tansaku()
        
        if (int(x/100))/(int(x%100))==3:
            print("{}/{}=13".format((int(x/100)),(int(x%100))))    

        undo(dy)
            
def move_to(dy):
    global move_vec
    global x
    x=int(10*x+dy)
    move_vec.remove(dy)

def undo(dy):
    global x
    x=int((x-dy)/10)
    move_vec.append(dy)
    move_vec.sort()

tansaku()

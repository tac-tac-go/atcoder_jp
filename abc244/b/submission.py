n = int(input())
s = input()

def posi_v(posi,x,y):
  if posi=="n":
    return x,y+1
  elif posi=="e":
    return x+1,y
  elif posi=="s":
    return x,y-1
  else:
    return x-1,y

now_x = 0
now_y = 0
now_posi = "e" #senw
for si in s:
  if si=="S":
    now_x,now_y = posi_v(now_posi,now_x,now_y)
  else:
    if now_posi=="n":
      now_posi = "e"
    elif now_posi=="e":
      now_posi = "s"
    elif now_posi=="s":
      now_posi = "w"
    else:
      now_posi = "n"
print(now_x,now_y)
    
    
  
  
  

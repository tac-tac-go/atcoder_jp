import math
n = int(input())
s = input()
win_c = [0,0]
j_w = math.ceil(n/2)
for i in s:
  if i=="T":win_c[0]+=1
  else :win_c[1]+=1
  
  if win_c[0]==j_w:
    print("T")
    break
  elif win_c[1]==j_w:
    print("A")
    break
    

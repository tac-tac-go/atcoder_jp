n = int(input())
array = [list(input()) for i in range(n)]
flag = True
for i in range(n):
  for j in range(n):
    if i!=j:
      if array[i][j]=="W":
        if array[j][i]!="L":
          flag = False
          break
      elif array[i][j]=="L":
        if array[j][i]!="W":
          flag = False
          break
      else:
        if array[j][i]!="D":
          flag = False
          break
  else:
    continue
  break
print("correct") if flag else print("incorrect")
        
        
  

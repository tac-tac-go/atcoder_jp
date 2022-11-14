import sys
N = int(input())
array = [list(input()) for i in range(N)]
array_j = ["".join(i) for i in array]
if len(set(array_j))!=len(array_j):
  print("No")
  sys.exit()

for i,j in array:
  if i not in ['H','D','C','S']:
      print("No")
      sys.exit()
  
  if j not in ['A','2','3','4','5','6','7','8','9','T','J','Q','K']:
      print("No")
      sys.exit()
print("Yes")

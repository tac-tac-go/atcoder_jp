n = int(input())
arr = {i+1:list(input()).count("o") for i in range(n)}
for i,j in sorted(arr.items(),key=lambda x:-x[1]):
  print(i,end=" ")

n,d = map(int,input().split())
array = [list(input()) for i in range(n)]
count = 0
max_v = 0
for i in range(d):
  tmp = []
  for j in range(n):
    if array[j][i]=="o":
      tmp.append(1)
    else:
      tmp.append(0)
  if all(tmp):
    count+=1
    if max_v<count:
      max_v = count
  else:
    count=0
print(max_v)

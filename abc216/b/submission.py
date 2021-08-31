n = int(input())
a = [input().split() for i in range(n)]
flag = False
for i in range(n):
  for j in range(i+1, n):
    if a[i][0] == a[j][0] and a[i][1] == a[j][1]:
      flag = True
      break
  if flag:
    break
print("Yes") if flag else print("No")

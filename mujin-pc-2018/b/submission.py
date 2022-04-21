count = 0
a = int(input())
s = input()
flag = False
for i in s:
  if a==0:
    flag = True
    break
  a+= 1 if i=="+" else -1
  a = max(a,0)

if a==0:
  print("Yes")
else:
  print("Yes") if flag else print("No")

a = int(input())
flag = False
for i in range(1, 101):
  if i**3==a:
      flag = True
      break
print("YES") if flag else print("NO")

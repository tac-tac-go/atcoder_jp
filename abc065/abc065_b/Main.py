n = int(input())
a = [int(input()) for i in range(n)]
count=1
flag=False
now =a[0]
for i in range(n):
  if now ==2:
    flag=True
    break
  count+=1
  now = a[now-1]
print(count) if flag else print(-1)
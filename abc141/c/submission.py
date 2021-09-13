n, k, q = map(int, input().split())
li = [0]*n
for i in range(q):
  a = int(input())
  li[a-1]+=1
for j in li:
  if q-j < k:print("Yes")
  else:print("No")
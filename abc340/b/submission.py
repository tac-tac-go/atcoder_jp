n = int(input())
result = []
for i in range(n):
  q1,q2 = input().split()
  if q1=="1":
    result.append(int(q2))
  else:
    print(result[-int(q2)])

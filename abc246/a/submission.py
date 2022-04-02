from collections import Counter
result1 = []
result2 = []
for i in range(3):
  x1,x2 = map(int,input().split())
  result1.append(x1)
  result2.append(x2)

print(sorted(Counter(result1).items(),key=lambda x:-x[1])[1][0],sorted(Counter(result2).items(),key=lambda x:-x[1])[1][0])

  

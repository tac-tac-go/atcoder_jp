n = input()
ai = list(map(int,input().split()))
result = [0]*30
for i in ai:
  result[i]+=1
print(*result)
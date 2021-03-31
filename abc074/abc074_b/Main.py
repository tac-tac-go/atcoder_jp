n = int(input())
k = int(input())
X = list(map(int,input().split()))
result=0
for x in X:
  result+=min(x*2,(k-x)*2)
print(result)
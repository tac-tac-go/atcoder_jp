N,M,X,Y = map(int, input().split())
Xi = list(map(int, input().split()))
Yi = list(map(int, input().split()))
result="War"
for Z in range(max(Xi)+1,min(Yi)+1):
  if X<Z<=Y:
    result="No War"
    break
print(result)
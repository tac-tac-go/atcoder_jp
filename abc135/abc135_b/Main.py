K = int(input())
P = list(map(int,input().split()))
cnt=0
for i in range(len(P)):
  if P[i]!=i+1:
    cnt+=1

print("YES") if cnt<=2 else print("NO")
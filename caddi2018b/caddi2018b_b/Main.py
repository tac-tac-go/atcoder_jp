N,H,W = map(int,input().split())
AB = [list(map(int,input().split())) for i in range(N)]
count = 0
for a,b in AB:
  if a>=H and b>=W:count+=1
print(count)
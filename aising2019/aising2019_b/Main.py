N = int(input())
A,B = map(int,input().split())
P = map(int,input().split())
cnt = [0]*3
for p in P:
  if p<=A:cnt[0]+=1
  elif A+1<=p<=B:cnt[1]+=1
  elif p>=B+1:cnt[2]+=1
print(min(cnt))
N,X = map(int,input().split())
S = list(map(int,input().split()))
a=[]
for s in S:
    if s!=X:
        a.append(s)
print(*a)
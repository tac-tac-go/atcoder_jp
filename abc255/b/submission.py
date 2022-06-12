N,K=map(int,input().split())
A=list(map(lambda x:int(x)-1,input().split()))
L=[]
for i in range(N):
    x,y=map(int,input().split())
    L+=[x,y],
X=[]
for a in A:
    X+=L[a],

INF=10**18
ANS=[INF]*N
for x1,y1 in X:
    for i,[x2,y2] in enumerate(L):
        ANS[i]=min(ANS[i],((x1-x2)**2+(y1-y2)**2)**.5)
print(max(ANS))


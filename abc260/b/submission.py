N,X,Y,Z=[int(nxyz) for nxyz in input().split()]
A=[int(a) for a in input().split()]
B=[int(b) for b in input().split()]

ans=[]
for x in range(X):
    AA=[]
    for i in range(N):
        if i not in ans:
            AA.append([A[i],-i])
    
    ans.append(-sorted(AA,reverse=True)[0][1])

for y in range(Y):
    BB=[]
    for j in range(N):
        if j not in ans:
            BB.append([B[j],-j])
    
    ans.append(-sorted(BB,reverse=True)[0][1])
    
    
for z in range(Z):
    C=[]
    for k in range(N):
        if k not in ans:
            C.append([A[k]+B[k],-k])
    
    ans.append(-sorted(C,reverse=True)[0][1])

[print(l+1) for l in sorted(ans)]





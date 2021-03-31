N=int(input())
X=list(map(int,input().split()))
X1=[];X2=[];M=0;Y=0;C=0
for i in range(N):
  X1.append(abs(X[i]))
  X2.append(abs(X[i])**2)
 
print(sum(X1))
print(sum(X2)**0.5)
print(max(X1))
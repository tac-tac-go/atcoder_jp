N,K = map(int,input().split())
if N==1:
    print(K)
else:
    count=0
    for i in range(N):
        if i==0:
            count=K
        else:
            count*=(K-1)
    print(count)
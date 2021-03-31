n=int(input())
l=list(map(int,input().split()))
k1=10**18
k=1
if 0 in l:
    print("0")
else:
    for i in range(0,n):
        k=k*l[i]
        if k>k1:
            k=-1
            break
    print(k)
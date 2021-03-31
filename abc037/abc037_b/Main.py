def resolve():
    n,q=map(int,input().split())
    a=[0]*n
    for i in range(q):
        l,r,t=map(int,input().split())
        a[l-1:r]=[t]*((r-l+1))
    print(*a,sep="\n")

resolve()
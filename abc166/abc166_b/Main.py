def resolve():
    import collections
    N,K = map(int,input().split())
    d = collections.defaultdict(int)
    
    for i in range(1,N+1):
        d[i]=0
    
    for i in range(0,K):
        a = int(input())
        b = list(map(int,input().split()))
        for j in b:
            d[j]+=1
    d = dict(d)
     
    print(len(list(filter(lambda x : x[1]==0,d.items()))))
        
resolve()
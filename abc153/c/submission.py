n,k = map(int,input().split())
Hn = sorted(map(int,input().split()))[::-1]
print(sum(Hn[k:]))

n,p,q=map(int,input().split())
array = list(map(int,input().split()))
print(min(p,q+min(array)))


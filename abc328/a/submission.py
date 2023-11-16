n,x = map(int,input().split())
arr = map(int,input().split())
print(sum(filter(lambda v:v<=x,arr)))

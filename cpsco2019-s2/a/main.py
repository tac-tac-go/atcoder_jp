m,n = map(int,input().split())
print(m-sum([m//n for i in range(1,n)]))
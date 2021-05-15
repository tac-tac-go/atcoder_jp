from functools import reduce
n = int(input())
print(*[reduce(lambda x,y:x*y,map(int,input().split())) for i in range(n)], sep='\n')
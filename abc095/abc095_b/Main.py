N,X = map(int,input().split())
m = [int(input()) for i in range(N)]
print(len(m)+((X-sum(m))//min(m)))
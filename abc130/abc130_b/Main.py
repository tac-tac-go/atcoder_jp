N,X = map(int,input().split())
L = list(map(int,input().split()))
result =[1 for i in range(len(L)+1) if sum(L[:i])<=X]
print(len(result))
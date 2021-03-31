N,K = map(int,input().split())
H = map(int,input().split())
print(len(list(filter(lambda x: x>=K,H))))
A,B,K = map(int,input().split())
AB_div = sorted([i for i in range(1,max(A,B)+1) if A%i==0 and B%i==0])[::-1]
print(AB_div[K-1])
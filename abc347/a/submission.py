n,k = map(int,input().split())
arr = list(map(int,input().split()))
print(" ".join([str(i//k) for i in arr if i%k==0]))

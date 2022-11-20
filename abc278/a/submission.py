n,k = map(int,input().split())
array = input().split()
print(" ".join(["0"]*n)) if n<=k else print(" ".join(array[k:]+["0"]*k))

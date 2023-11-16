n = int(input())
arr = list(map(int,input().split()))
print(list(set(range(min(arr),max(arr)+1))-set(arr))[0])


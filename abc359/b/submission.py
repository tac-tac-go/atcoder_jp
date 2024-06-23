n = int(input())
arr = list(map(int,input().split()))
print(sum([1 for i in range(0,len(arr)-2) if arr[i+2]==arr[i]]))

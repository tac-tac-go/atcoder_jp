n = int(input())
arr = list(map(int,input().split()))
print(" ".join(map(str,[arr[i]*arr[i+1] for i in range(0,len(arr)-1)])))

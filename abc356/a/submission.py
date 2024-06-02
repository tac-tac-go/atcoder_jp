n,l,r = map(int,input().split())
arr = list(range(1,n+1))
arr_s = sorted(arr[l-1:r])[::-1]
arr[l-1:r] = arr_s
print(" ".join(map(str,arr)))

n = int(input())
arr = list(map(int,input().split()))
arr_s = sorted(arr)[::-1]
print(arr.index(arr_s[1])+1)

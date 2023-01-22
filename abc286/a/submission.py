n,p,q,r,s = map(int,input().split())
array = list(map(int,input().split()))
tmp = array[p-1:q]
tmp2 = array[r-1:s]
array[r-1:s] = tmp
array[p-1:q] = tmp2
print(*array)


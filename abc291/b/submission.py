n = int(input())
xarray = sorted(map(int,input().split()))
ave = xarray[2*n-n:-2*n+n]
print(sum(ave)/len(ave))


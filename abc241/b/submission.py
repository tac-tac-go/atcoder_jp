n,m = map(int,input().split())
an = list(map(int,input().split()))
bn = list(map(int,input().split()))
bn_c = list(bn)
for v in bn_c:
  if v in bn and v in an:
    del bn[bn.index(v)]
    del an[an.index(v)]
  else:
    print("No")
    exit()
print("Yes")

H,W = map(int,input().split())
l = [list(map(int,input().split())) for l in range(H)]
l_flatten = sum(l,[])
value=0
for l_v in l_flatten:
    value+=(l_v-min(l_flatten))
print(value)
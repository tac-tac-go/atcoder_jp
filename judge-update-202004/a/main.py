s,l,r = map(int,input().split())
print(min(l,r)) if min(l,r)>=s else print(max(l,r)) if max(l,r)<=s else print(s)
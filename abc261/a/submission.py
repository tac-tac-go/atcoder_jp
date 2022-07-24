v1,v2,v3,v4 = map(int,input().split())
print(len(list(set(range(v1,v2))&set(range(v3,v4)))))

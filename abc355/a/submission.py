AB = list(map(int,input().split()))
result = list(set(range(1,4)) - set(AB))
print(-1) if len(result)>1 else print(result[0])

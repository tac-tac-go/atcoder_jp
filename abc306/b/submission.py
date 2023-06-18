array = map(int,input().split())
print(sum([v*(2**i) for i,v in enumerate(array)]))

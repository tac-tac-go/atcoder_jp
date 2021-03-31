from collections import Counter
A,B,C = map(int,input().split())
c = Counter([A,B,C])
c = sorted(c.items(),key = lambda x: x[1])
print(c[0][0])
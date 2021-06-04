n = int(input())
p = tuple(map(int,input().split()))
ans = set([0])
for i in range(n):
    for jsum in list(ans):
        ans |= set([jsum + p[i]])
print(len(ans))
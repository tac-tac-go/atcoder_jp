n, k = map(int, input().split())
an = sorted([int(input()) for i in range(n)])[::-1]
print(sum(an[:k])+sum(map(lambda x: x*2, an[k:])))

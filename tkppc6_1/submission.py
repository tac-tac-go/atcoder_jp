n, m = map(int, input().split())
an = map(int, input().split())
print(min(len(set(an))+m, n))

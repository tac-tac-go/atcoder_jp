n, k = map(int, input().split())
an = list(map(int, input().split()))
bn = sorted(an)
q, mod = divmod(k, n)
result = {}
for i in bn:
  result[i] = q
for i in range(0, mod, 1):
  result[bn[i]] += 1
for i in an:
  print(result[i])

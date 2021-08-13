n, m = map(int, input().split())
an = list(sorted(map(int, input().split())))[::-1]
kind = 0
for i in an:
    if m <= 0:
      break
    else:
        m -= i
        kind += 1
print(kind)

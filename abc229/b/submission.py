a, b = input().split()
a = a.zfill(max(len(a), len(b)))
b = b.zfill(max(len(a), len(b)))
result = "Easy"
for ai, bi in zip(a, b):
  if int(ai)+int(bi) >= 10:
    result = "Hard"
    break
  else:
    continue
print(result)

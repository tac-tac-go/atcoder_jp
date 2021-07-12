n, x = map(int, input().split())
an = list(map(int, input().split()))
count = 0
for i, v in enumerate(an):
  if i % 2 == 0:
    count += an[i]
  else:
    count += an[i]-1
print("Yes") if x >= count else print("No")

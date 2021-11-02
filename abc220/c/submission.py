n = int(input())
an = list(map(int, input().split()))
x = int(input())
an_s = sum(an)
count = x//an_s
result = count*len(an)
rest = x - (an_s)*count
for i, v in enumerate(an):
  if rest < 0:
    break
  else:
    rest -= v
    result += 1
print(result)

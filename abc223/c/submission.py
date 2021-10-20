N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
s = sum([A/B for A, B in AB])/2
length = 0
for A, B in AB:
  if A/B <= s:
    s -= A/B
    length += A
  else:
    length += s*B
    break
print(length)

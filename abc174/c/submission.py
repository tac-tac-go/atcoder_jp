K = int(input())
count = 1
mod = 7

for i in range(K):
  if mod % K == 0:
    break
  count += 1
  mod = (mod * 10 + 7) % K

if mod % K == 0:
  print(count)
else:
  print(-1)

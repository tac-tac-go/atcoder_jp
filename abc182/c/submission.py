n = input()
cnt = [0] * 3
for c in n:
    d = ord(c) - ord('0')
    cnt[d % 3] += 1

now = (cnt[1] + cnt[2] * 2) % 3

def solve():
    if now == 0:
      return (0)
    elif now == 1:
        if cnt[1] >= 1:
          return (1)
        elif cnt[2] >= 2:
          return (2)
    else:
        if cnt[2] >= 1:
          return (1)
        elif cnt[1] >= 2:
          return (2)

ans = solve()

if ans == len(n):
    print(-1)
else:
    print(ans)

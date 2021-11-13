N = int(input())
tlr = []
for _ in range(N):
    t, l, r = map(float, input().split())
    if t == 2:
        r -= 0.1
    if t == 3:
        l += 0.1
    if t == 4:
        l += 0.1
        r -= 0.1
    tlr.append((l, r))
tlr.sort()
count = 0
for i in range(len(tlr)-1):
    for j in range(i+1, len(tlr)):
        l1, r1 = tlr[i]
        l2, r2 = tlr[j]
        if l2 <= r1:
            count += 1
print(count)

n = int(input())
ans = 100
for a in range(26):
    for b in range(26):
        if (n - (8 * a + 10 * b)) % 26 == 0:
            ans = min(ans, a + b)
print(ans)

n = int(input())
cnt = 0
ans = ''
while n > 0:
    if n % 2 == 1:
        n -= 1
        ans += 'A'
    else:
        n //= 2
        ans += 'B'
print(''.join(list(reversed(ans))))
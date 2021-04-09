N = int(input())
A = list(map(int, input().split()))
A = list(filter(lambda x: x % 2 == 0, A))

ans = 0
for a in A:
    while a % 2 == 0:
        a = a // 2
        ans += 1
print(ans)
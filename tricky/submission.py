N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    ans = abs(A) // abs(B)
    if A * B > 0:
        print(ans)
    else:
        print(-ans)

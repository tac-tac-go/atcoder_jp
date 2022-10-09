N, M = map(int, input().split())
L = [[False] * N for _ in range(N)]
for _ in range(M):
    k, *X = map(int, input().split())
    for i in range(k):
        for j in range(k):
            L[X[i]-1][X[j]-1] = True
            L[X[j]-1][X[i]-1] = True

for i in range(N):
    for j in range(i+1,N):
        if not L[i][j]:
            print("No")
            exit()
print("Yes")


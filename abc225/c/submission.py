yes, no = 'Yes', 'No'
N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]
f = B[0][0]
if (f-1) % 7+M > 7:
    print(no)
    exit()
for i in range(N):
    for j in range(M):
        if B[i][j] != f+i*7+j:
            print(no)
            exit()
print(yes)

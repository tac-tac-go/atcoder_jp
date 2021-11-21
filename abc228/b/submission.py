N, X = map(int, input().split())
A = [0]+list(map(int, input().split()))
Y = [False]*(N+1)
cnt = 0
while Y[X] == False:
    Y[X] = True
    X = A[X]
    cnt += 1
print(cnt)

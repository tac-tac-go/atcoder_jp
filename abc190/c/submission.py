N, M = map(int, input().split())
zyouken = []
for i in range(M):
    a, b = map(int, input().split())
    zyouken.append([a, b])
K = int(input())
okikata = []
for i in range(K):
    c, d = map(int, input().split())
    okikata.append([c, d])
maximum = -9999
for i in range(2**K):
    f = "{{:0{}b}}".format(K)
    judge = f.format(i)
    ball = [0 for i in range(N)]
    for j in range(K):
        if judge[j] == "1":
            ball[okikata[j][0]-1] += 1
        else:
            ball[okikata[j][1]-1] += 1
    now = 0
    for j in range(M):
        if ball[zyouken[j][0]-1] >= 1 and ball[zyouken[j][1]-1] >= 1:
            now += 1
    if now > maximum:
        maximum = now
print(maximum)

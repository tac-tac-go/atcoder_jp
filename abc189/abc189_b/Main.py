N,X = map(int,input().split())
R = [list(map(int,input().split())) for i in range(N)]
count=-1;drink=0
for i in range(N):
    drink+=R[i][0]*(R[i][1])
    if drink>X*100:
        count=i+1
        break
print(count)
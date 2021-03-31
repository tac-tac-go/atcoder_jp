N = int(input())
R = [list(map(int,input().split())) for i in range(N)]
count=0
for i in range(N-1):
    for j in range(i+1,N):
            if -1<=(R[j][1]-R[i][1])/(R[j][0]-R[i][0])<=1:
                count+=1
print(count)
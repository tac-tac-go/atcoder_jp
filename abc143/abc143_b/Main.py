N = int(input())
D = list(map(int,input().split()))
sum_v = 0
for i in range(N-1):
    for j in range(i+1,N):
        sum_v+=(D[i]*D[j])
print(sum_v)
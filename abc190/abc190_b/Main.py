N,S,D = map(int,input().split())
R = [list(map(int,input().split())) for i in range(N)]
result="No"
for i,j in R:
    if i<S and D<j:result="Yes"
print(result)
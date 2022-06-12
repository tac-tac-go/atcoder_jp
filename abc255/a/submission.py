r,c = map(int,input().split())
array = [list(map(int,input().split())) for i in range(2)]
print(array[r-1][c-1])

n,m = map(int,input().split())
a_array = list(map(int,input().split()))
b_array = list(map(int,input().split()))
print(sum([a_array[i-1] for i in b_array]))

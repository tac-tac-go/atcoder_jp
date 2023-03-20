n = int(input())
array = list(map(int,input().split()))
print(" ".join([str(i) for i in array if i%2==0]))

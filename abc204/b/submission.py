n = int(input())
an = list(map(int,input().split()))
print(sum([(i-10) for i in an if i>=10]))

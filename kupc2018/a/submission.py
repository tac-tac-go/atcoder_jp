n = int(input())
s = list(map(int, input().split()))
a = list(map(int, input().split()))
print(max([i*j for i, j in zip(s, a)]))

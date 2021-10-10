n, p = map(int, input().split())
an = map(int, input().split())
print(len([i for i in an if i < p]))

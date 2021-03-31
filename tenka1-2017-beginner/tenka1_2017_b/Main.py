n = int(input())
AB = [list(map(int,input().split())) for _ in range(n)]
AB.sort()
print(AB[-1][0]+AB[-1][1])
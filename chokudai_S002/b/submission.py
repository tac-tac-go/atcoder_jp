n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
surplus = [print(i[0] % i[1]) for i in ab]

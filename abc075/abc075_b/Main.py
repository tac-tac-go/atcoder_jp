h, w = map(int, input().split())
l = []
for _ in range(h):
    l.append(input())
# print(*l,sep='\n')
# print('--------------')

dx = [1,0,-1,0,1,-1,-1,1]
dy = [0,1,0,-1,1,1,-1,-1]

for i in range(h):
    line = ''
    for j in range(w):
        if l[i][j] != '#':
            cnt = 0
            for k in range(len(dx)):
                ni = i + dy[k]
                nj = j + dx[k]
                if ni < 0 or h <= ni:
                    continue
                if nj < 0 or w <= nj:
                    continue
                if l[ni][nj] == '#':
                    cnt += 1
            line += str(cnt)
        else:
            line += '#'
    print(line)
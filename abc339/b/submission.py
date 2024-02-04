h, w, n = map(int, input().split())
x = 0
y = 0
d = 0

grid = [["."]*w for i in range(h)]

for i in range(n):
    if grid[x][y] == ".":
        grid[x][y] = "#"
        if d == 0:
            y = (y+1) % w
        elif d == 1:
            x = (x+1) % h
        elif d == 2:
            y = (y-1) % w
        elif d == 3:
            x = (x-1) % h
        d = (d+1)%4

    elif grid[x][y] == "#":
        grid[x][y] = "."
        if d == 0:
            y = (y-1) % w
        elif d == 1:
            x = (x-1) % h
        elif d == 2:
            y = (y+1) % w
        elif d == 3:
            x = (x+1) % h

        d = (d-1) % 4      

for i in grid:
    print(''.join(i))
    

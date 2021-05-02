n,d,h = map(int,input().split())
d_h = [list(map(int,input().split())) for i in range(n)]
max_y = 0.0
for d_i,h_i in d_h:
    ratio = h/d
    if ratio*d_i>=h_i:continue
    else:
        a = (h-h_i)/(d-d_i)
        b = h_i-(d_i*a)
        if b > max_y:
            max_y = b
print(max_y)
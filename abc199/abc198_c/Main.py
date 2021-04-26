n = int(input())
s = list(input())
q = int(input())

result = s
flip_flag = False

for i in range(q):
    t,a,b = map(int, input().split())
    a -= 1
    b -= 1
    if t == 1:
        if flip_flag:
            result[a-n], result[b-n] = result[b-n], result[a-n]
        else:
            result[a], result[b] = result[b], result[a]
    else:
        flip_flag = not flip_flag

if flip_flag:
    result = result[n:] + result[:n]
print(''.join(result))
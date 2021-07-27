a = int(input())
b = int(input())
for i in range(a, 0, -1):
    if i % b == 0:
        print(i)
        break

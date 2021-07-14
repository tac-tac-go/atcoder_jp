n = int(input())
print(100-len([i for i in range(1, 101) if i % n == 0]))

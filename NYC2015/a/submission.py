n = int(input())
binary = format(n, 'b')
print("Yes") if binary == binary[::-1] else print("No")

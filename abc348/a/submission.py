n = int(input())
print("".join(["x" if (i+1)%3==0 else "o" for i in range(n)]))

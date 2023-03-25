array = "and, not, that, the, you".split(", ")
n = int(input())
words = input().split()
result = [word for word in words if word in array]
print("Yes") if len(result)>=1 else print("No")

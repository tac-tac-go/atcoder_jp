a, b = map(int, input().split())
print("Gold") if a > 0 and b == 0 else print(
    "Silver") if a == 0 and b > 0 else print("Alloy")

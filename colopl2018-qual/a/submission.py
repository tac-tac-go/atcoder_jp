a, b = map(int, input().split())
s = input()
print("YES") if a <= len(s) and len(s) <= b else print("NO")

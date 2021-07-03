s = input()
print("YES") if s[:3] == "yah" and len(set(s[3:])) == 1 else print("NO")

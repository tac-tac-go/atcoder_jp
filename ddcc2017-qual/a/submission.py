s = input()
print("Yes") if len(set(s[:2])) == 1 and s[1] != s[2] and len(set(s[2:])) == 1 else print("No")

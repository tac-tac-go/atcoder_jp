s = input()
t = input()
print("same") if s == t else print(
    "case-insensitive") if s.lower() == t.lower() else print("different")

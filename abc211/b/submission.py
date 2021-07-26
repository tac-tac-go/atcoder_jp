array = ["H", "2B", "3B", "HR"]
s = [input(), input(), input(), input()]
array.sort()
s.sort()
print("Yes") if "".join(array) == "".join(s) else print("No")

import re
s = input()
print("Yes") if re.search(r'^<=+>$',s) else print("No")

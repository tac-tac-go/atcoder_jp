import re
s = input()
reg = r'^A?KIHA?BA?RA?$'
search = re.search(reg, s)
if search:
  print("YES")
else:
  print("NO")

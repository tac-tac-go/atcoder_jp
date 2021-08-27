import re
n = int(input())
pattern = ".*okyo.*ech.*"
for i in range(n):
  s = input()
  flag = re.match(pattern, s)
  if flag != None:
    print("Yes")
  else:
    print("No")

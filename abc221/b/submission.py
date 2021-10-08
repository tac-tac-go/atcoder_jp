s = input()
t = input()
flag = False
if s == t:
    print("Yes")
else:
  for i in range(0, len(s)-1):
      if s[:i]+s[i:i+2][::-1]+s[i+2:] == t:
          flag = True
          break
  print("Yes") if flag else print("No")

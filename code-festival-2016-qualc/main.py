s = input()
if "C" in s:
  c_i = s.index("C")
  result="No"
  for i in range(c_i+1,len(s)):
    if s[i]=="F":
      result="Yes"
      break
  print(result)
else:
  print("No")
s = list(input())
result = ''
for si in s:
  if si == "0":
    result += "0"
  elif si == "1":
    result += "1"
  else:
    result = result[:len(result)-1]
print(result)

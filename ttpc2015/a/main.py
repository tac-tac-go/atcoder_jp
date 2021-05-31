s = input()
y = s[:2]
g = s[2]
if g == "B":
  print("Bachelor",y)
elif g == "M":
  print("Master",y)
else:
  print("Doctor",y)
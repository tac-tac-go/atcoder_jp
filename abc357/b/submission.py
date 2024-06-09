s = input()
lower = 0
upper = 0
for i in s:
  if i.isupper():
    upper+=1
  else:
    lower+=1
print(s.upper()) if upper>lower else print(s.lower())

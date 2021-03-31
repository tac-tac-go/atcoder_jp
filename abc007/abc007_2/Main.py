import string
lower = list(string.ascii_lowercase)
a = input()
if len(a)>=2:
  print(a[:-1])
elif a=="a":
  print(-1)
else:
  print(lower[lower.index(a)-1])
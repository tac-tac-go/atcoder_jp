def resolve():
  a,b = input().split()
  flag=True
  if a=="H":
      if b=="D":flag=False
  else:
      if b=="H":flag=False
  print("H" if flag else "D")

resolve()
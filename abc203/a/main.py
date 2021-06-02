abc_b = list(input().split())
abc = list(set(abc_b))
if len(abc)==3:
  print(0)
else:
  if abc_b[0]==abc_b[1]:
    print(abc_b[2])
  elif abc_b[0]==abc_b[2]:
    print(abc_b[1])
  else:
    print(abc_b[0])
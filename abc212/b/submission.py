X = list(map(int, list(input())))
if(len(set(X)) == 1):
  print("Weak")
else:
  X1 = ((X[0]+1) % 10) == X[1]
  X2 = ((X[1]+1) % 10) == X[2]
  X3 = ((X[2]+1) % 10) == X[3]
  if(X1 and X2 and X3):
    print("Weak")
  else:
    print("Strong")

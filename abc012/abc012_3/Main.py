n = int(input())
diff = 2025-n
count=1
for i in range(1,10):
  for j in range(1,10):
    if i*j ==diff:
      print("{} x {}".format(i,j))
      count+=1
n = int(input())
while True:
  if int(str(n)[0])*int(str(n)[1]) == int(str(n)[2]):
    print(n)
    break
  else:
    n+=1

N = int(input())
result ="-1"
for i in range(1,38):
  for j in range(1,26):
    if 3**(i)+5**(j)==N:
      result="{} {}".format(i,j)
      break
  else:
    continue
  break
print(result)
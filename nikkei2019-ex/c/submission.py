s = input()[::-1]
sum_o = 0
sum_e = 0
for i,v in enumerate(s):
  if (i+1)%2==1:
    sum_o += int(v)
  else:
    sum_e += int(v)
print((sum_o-sum_e)%11)

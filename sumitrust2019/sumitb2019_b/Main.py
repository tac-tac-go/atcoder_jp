n = int(input())
se = int(n/1.08)
result = ":("
for i in range(se-3,se+3):
  if int(i*1.08)==n:result=i
print(result)
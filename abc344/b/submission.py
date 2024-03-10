n = [int(input())]
while n[-1]!=0:
  n.append(int(input()))
for i in n[::-1]:
  print(i)
  

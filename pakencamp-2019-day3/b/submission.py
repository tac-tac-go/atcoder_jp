n = int(input())
black=0;white=0
for i in range(n):
  s = input()
  if s=="black":black+=1
  else : white+=1
print("black") if black>white else print("white")
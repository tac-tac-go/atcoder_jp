N = int(input())
A = input()
B = input()
C = input()
count=0
for a,b,c in zip(A,B,C):
  abc = len(set([a,b,c]))
  if abc==2:
    count+=1
  elif abc==3:
    count+=2
print(count)    
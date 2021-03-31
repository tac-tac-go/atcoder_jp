N = int(input())
S = input()
record=[0]
number=0
for i in range(len(S)):
  if S[i]=="I":
    number+=1
    record.append(number)
  else:
    number-=1
    record.append(number)
print(max(record))
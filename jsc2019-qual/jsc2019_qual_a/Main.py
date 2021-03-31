M,D = map(int,input().split())
count=0
for i in range(1,M+1):
  for j in range(20,D+1):
    if int(str(j)[0])>=2 and int(str(j)[1])>=2 and int(str(j)[0])*int(str(j)[1])==i:
      count+=1
print(count)
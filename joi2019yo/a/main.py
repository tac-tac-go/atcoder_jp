a,b,c = map(int,input().split())
result=0
index=0
while result<c:
  result+=a
  if (index+1)%7==0:result+=b
  index+=1
print(index)
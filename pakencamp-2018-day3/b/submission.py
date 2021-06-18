n = int(input())
year=0;count=0
for i in range(n):
  year+=int(input()) 
  if year <=2018:count+=1
print(count)
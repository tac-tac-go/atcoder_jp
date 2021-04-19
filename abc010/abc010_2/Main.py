n = int(input())
a = list(map(int,input().split()))
count=0
for a_i in a:
  while a_i%2==0 or (a_i-2)%3==0:
    a_i-=1
    count+=1  
print(count)
n = int(input())
if n%2==1:
  print("error")
else:
  if n==2:
    a,b = map(int,input().split())
    print(b-a)
  else:
    array = list(map(int,input().split()))
    count = array[-1]-array[0]
    for i in range(2,n,2):
      count -= (array[i]-array[i-1])
    print(count)
      
      

n,m = map(int,input().split())
array = [list(input()) for i in range(n)]
count = 0
for i in range(len(array)-1):
  for j in range(i+1,len(array)):
    p = True
    for p1,p2 in zip(array[i],array[j]):
      if p1=='x' and  p2=='x':
        p = False
    if p:
      count += 1
print(count)
    
    
        
    
                  

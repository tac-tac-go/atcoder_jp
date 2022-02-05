n = int(input())
array = [list(map(int,input().split())) for i in range(n)]
max_v = 0
for i in range(len(array)-1):
  for j in range(i+1,len(array)):
    c1 = array[i]
    c2 = array[j]
    v = (((c1[0]-c2[0])**2)+((c1[1]-c2[1])**2))**0.5
    if v>max_v:
      max_v = v
print(max_v)
    
    

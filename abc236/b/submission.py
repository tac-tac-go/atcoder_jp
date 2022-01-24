n = int(input())
an = map(int,input().split())
array = [0]*n
for i in an:
  array[i-1]+=1
print([i+1 for i,x in enumerate(array) if x!=4][0])



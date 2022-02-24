from itertools import permutations
n = int(input())
array = [list(map(int,input().split())) for i in range(n)]
p = list(permutations(range(1,n+1),n))
result = []
for pi in p:
  value=0
  for i in range(len(pi)-1):
    x = (array[pi[i]-1][0]-array[pi[i+1]-1][0])**2
    y =  (array[pi[i]-1][1]-array[pi[i+1]-1][1])**2
    value+=(x+y)**0.5
  result.append(value)
print(sum(result)/len(result))

    

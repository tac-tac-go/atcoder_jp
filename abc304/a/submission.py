n = int(input())
array = [input().split() for i in range(n)]
name = [i for i,_ in array]
array_c = name+name
min_i = ([int(j) for _,j in array])
min_v = min_i.index(min(min_i))
for i in range(min_v,min_v+n):
  print(array_c[i])


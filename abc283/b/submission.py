n = int(input())
array = list(map(int,input().split()))
q = int(input())
query = [list(map(int,input().split())) for i in range(q)]
for i in query:
  if i[0] == 1:
    index = i[1]
    v = i[2]
    array[index-1] = v
  else:
    print(array[i[1]-1])


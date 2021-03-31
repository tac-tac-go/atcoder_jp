import itertools,math
x_y = [list(map(int,input().split())) for i in range(int(input()))]
array = []
for x,y in itertools.combinations(x_y,2):
  result =list(map(lambda x,y:abs(x-y),x,y))
  array.append(math.sqrt(sum(list(map(lambda x:x**2,result)))))

print(max(array))
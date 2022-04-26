def recursive(num):
  if num==1:return 1
  return [recursive(num-1),num,recursive(num-1)]

n = int(input())
result = recursive(n)
list_str = str(result).replace("[", "").replace("]", "").split(",")
print(*list_str)

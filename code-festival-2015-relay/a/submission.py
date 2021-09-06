t = int(input())
num1 = t
num2 = 40-t+1
result = [num1, num2]
add = 40
for i in range(4):
  result.append(num1+add)
  result.append(num2+add)
  add += 40
print(sum(result))

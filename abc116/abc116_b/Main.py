S = int(input())
result=[S]
for i in range(1000001):
  if result[-1]%2==0:
    result.append(result[-1]//2)
  else:
    result.append(result[-1]*3+1)

  if result[-1] in result[:-1]:
    print(len(result))
    break
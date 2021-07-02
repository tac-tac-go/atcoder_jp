def prime_check(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input())
result = []
for x in range(2, n+1):
  if prime_check(x):
      result.append(x)
print(len(list(filter(lambda x: x%2 == 0, result))))

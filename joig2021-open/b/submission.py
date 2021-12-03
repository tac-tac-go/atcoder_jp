def judge(char):
  if char.islower():
      return char.upper()
  else:
    return char.lower()

n, k = map(int, input().split())
t = input()
if n == 1:
  result = judge(t)
  print(result)
else:
  result = t[:k-1]
  for i in range(k-1, n):
    char = t[i]
    judge_t = judge(char)
    result += judge_t
  print(result)

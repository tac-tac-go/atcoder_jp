target = 'keyence'
s = input()
result ="NO"
for i in range(0,8):
  if s[:i] + s[i-7:]==target:
    result = "YES"
print(result)

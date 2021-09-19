s = [input(),input(),input()]
tn = map(int,list(input()))
result=""
for t in tn:
  result+=s[t-1]
print(result)
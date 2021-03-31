from collections import Counter
W = dict(Counter(list(input())))
result = "Yes"
for i,v in W.items():
  if v%2!=0:result="No";break
print(result)
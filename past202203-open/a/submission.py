abc = list(sorted(map(int,input().split())))
result = []
for i in range(len(abc)):
  for j in range(len(abc)):
    if i!=j:
      result.append(abc[i]*abc[j])
print(min(result),max(result))

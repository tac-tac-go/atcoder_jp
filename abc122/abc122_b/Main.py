S = input()
count=0
ans=0
for s in S:
  if s in ['A',"C","G","T"]:
    count+=1
    if count>ans:
      ans = count
  else:
    count=0
print(ans)
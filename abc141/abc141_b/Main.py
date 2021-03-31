S = input()
result='Yes'
for i,v in enumerate(S):
  if (i+1)%2==0 and v in ["L","U","D"]:
    continue
  elif (i+1)%2==1 and v in ["R","U","D"]:
    continue
  else:
    result="No"
    break
print(result)
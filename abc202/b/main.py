s= list(input())[::-1]
for i,s_i in enumerate(s):
  if(s_i=="6"):s[i]=9
  elif(s_i=="9"):s[i]=6
s = list(map(str,s))
print("".join(s))
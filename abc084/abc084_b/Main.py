A,B = map(int,input().split())
S = input().split("-")
if len(S)!=2:print("No")
else:
  if len(S[0])!=A or len(S[1])!=B:print("No")
  elif (not (S[0].isdigit())) or (not (S[1].isdigit())):print("No")
  else:print("Yes")
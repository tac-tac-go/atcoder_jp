S = input()
YY = int(S[:2]);MM=int(S[2:])
if 1<=YY<=12:
  if 1<=MM<=12:print("AMBIGUOUS")
  else:print("MMYY")
else:
  if 1<=MM<=12:print("YYMM")
  else : print("NA")
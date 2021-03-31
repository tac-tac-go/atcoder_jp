S = list(input())
T = list(input())
result = "You can win"
for i1,i2 in zip(S,T):
  if i1!="@" and i2!="@":
    if i1!=i2:result="You will lose";break
  elif i1!="@" and i2=="@":
    if i1 not in ["a","t","c","o","d","e","r"]:
      result="You will lose";break
  elif i1=="@" and i2!="@":
    if i2 not in ["a","t","c","o","d","e","r"]:
      result="You will lose";break
print(result)
n,a,b = map(int,input().split())
s = list(input())
pass_c =0
pass_f =0
for i,s_v in enumerate(s):
  if s_v =="a":
    if pass_c<a+b:
      print("Yes")
      pass_c+=1
    else:
      print("No")
  elif s_v=="b":
    if pass_c<a+b and (pass_f<b):
      print("Yes")
      pass_c+=1
      pass_f+=1
    else:
      print("No")
  else:
    print("No")
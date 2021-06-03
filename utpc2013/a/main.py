o_0 = list('CEFGHIJKLMNSTUVWXYZ')
o_1 = list('ADOPQR')
s = list(input())
if s[0] in o_0 and s[1] in o_0 and s[2] in o_1 and s[3] in o_0:
  print("yes")
else:
  print("no")
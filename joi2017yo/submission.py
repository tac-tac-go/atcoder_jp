a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a < 0:
  print(abs(a*c)+d+abs(b*e))
elif a == 0:
  print(d+(b*e))
else:
  print((b-a)*e)

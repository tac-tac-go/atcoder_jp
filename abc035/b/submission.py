S = input().rstrip()
t = int(input())

h = 0
dx = 0
dy = 0

for i in range(len(S)):
  if S[i] == "L":
    dx -= 1
  if S[i] == "R":
    dx += 1
  if S[i] == "U":
    dy += 1
  if S[i] == "D":
    dy -= 1
  if S[i] == "?":
    h += 1

    
if t == 1:
  print(abs(dx)+abs(dy)+h)
else:
  if abs(dx)+abs(dy)-h >= 0:
    print(abs(dx)+abs(dy)-h)
  else:
    if (abs(dx)+abs(dy)-h)%2 == 0:
      print(0)
    else:
      print(1)

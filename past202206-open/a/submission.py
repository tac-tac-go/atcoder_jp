X,A,B,C = map(int,input().split())
A_time = X/A + C
B_time = X/B
if A_time==B_time:
  print("Tie")
elif A_time < B_time:
  print("Hare")
else:
  print("Tortoise")

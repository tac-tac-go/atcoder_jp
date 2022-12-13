import sys
S = input()
num = S[1:-1]

if len(S) != 8:
  print("No")
  sys.exit()

if S[0].isupper() and S[-1].isupper() and num.isdigit():
  num = int(num)
  if 100000<=num and num<=999999:
    print("Yes")
    sys.exit()
print("No")

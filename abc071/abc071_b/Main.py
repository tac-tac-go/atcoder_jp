import string,sys
alpha = list(string.ascii_lowercase)
S = sorted(list(input()))
R = 'None'
for s in alpha:
  if s not in S:
    print(s)
    sys.exit()
print(R)
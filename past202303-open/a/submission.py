N,S,T=map(int,input().split())
if S==0:
  first = "Alice"
  second = "Bob"
else:
  first = "Bob"
  second = "Alice"
if T==0:
  if N%2==0:
    print(second)
  else:
    print(first)
else:
  if N%2==0:
    print(first)
  else:
    print(second)

N = int(input())
while True:
  if len(set(list(str(N))))!=1:
    N+=1
  else:
    break
print(N)
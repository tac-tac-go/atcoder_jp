n = input()
search1 = n[1:]
search2 = "9"*len(n[1:])
if search1<search2:
  print((int(n[0])-1)+sum(map(int,list(search2))))
else:
  print((int(n[0]))+sum(map(int,list(search2))))
  

s = input()
t = input()
current_s = 0
for i,v in enumerate(t):
  if v==s[current_s]:
    print(i+1)
    current_s +=1
  
  

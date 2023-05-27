import sys
n = int(input())
input1 = input()
input2 = input()
for s1,s2 in zip(input1,input2):
  if s1==s2 or \
  (s1=="1" and s2=="l") or \
  (s1=="l" and s2=="1") or \
  (s1=="0" and s2=="o") or \
  (s1=="o" and s2=="0"):
    continue
  else:
    print("No")
    sys.exit()
print("Yes")
  

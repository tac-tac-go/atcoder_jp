a = int(input())
b = int(input())
c = int(input())
s = int(input())
q1 = [a, a+1]
q2 = [b, b+1]
q3 = [c, c+1]
flag = False
for i1 in q1:
  for i2 in q2:
    for i3 in q3:
      if i1+i2+i3 == s:
          flag = True
          break
print("Yes") if flag else print("No")

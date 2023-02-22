n,k = map(int,input().split())
s = input()
count = 0
result = ""
for si in s:
  if si=="o" and count<k:result+="o";count+=1
  else:
   		result += "x"
print(result)

s = input()
flag = "Yes"
for i in range(0,len(s)-1):
  if s[i] <= s[i+1]:
    flag = "No"
    break
print(flag)


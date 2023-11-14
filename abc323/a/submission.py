s = input()[::-1]
result = [True if s[i]=="0" else False for i in range(0,len(s),2)]
print("Yes") if all(result) else print("No")

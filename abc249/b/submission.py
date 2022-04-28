s = input()	
result = len([1 for i in list(s) if i.isupper()])>0
result2 = len([1 for i in list(s) if i.islower()])>0
result3 = len(set(list(s))) == len(s)
print("Yes") if result and result2 and result3 else print("No")

S = input()
result="Yes"
for i,v in enumerate(S):
    if i%2==0:
        if not(v.islower()):
            result="No"
            break
    else:
        if not(v.isupper()):
            result="No"
            break
print(result)
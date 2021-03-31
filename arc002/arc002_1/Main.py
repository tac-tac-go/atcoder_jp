Y = int(input())
result = "NO"
if Y%4==0:
    result = "YES"
    if Y%400==0:
        result="YES"
    elif Y%100==0:
        result="NO"  
else:
    result="NO"
print(result)
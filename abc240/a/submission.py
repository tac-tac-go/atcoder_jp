a,b = map(int,input().split())
print("Yes") if abs(a-b)==1 or (min(a,b)==1 and max(a,b)==10) else print("No")

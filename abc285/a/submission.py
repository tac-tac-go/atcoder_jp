a,b = map(int,input().split())
print("Yes") if min(a,b)*2 == max(a,b) or min(a,b)*2+1 == max(a,b) else print("No")

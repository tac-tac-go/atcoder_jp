A,B,C = map(int,input().split())
print("Yes") if C in list(range(min(A,B),max(A,B)+1)) else print("No")
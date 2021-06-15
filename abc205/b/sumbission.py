n = int(input())
a = list(map(int,input().split()))
print("Yes") if len(set(list(range(1,n+1)))-set(a))==0 else print("No")
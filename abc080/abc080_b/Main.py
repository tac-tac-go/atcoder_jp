N = int(input())
print("Yes") if N%sum(map(int,list(str(N))))==0 else print("No")
N = int(input())
A= map(int,input().split())
B= map(int,input().split())
print("Yes")if sum([i*j for i,j in zip(A,B)])==0 else print("No")
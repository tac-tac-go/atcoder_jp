H, N = map(int, input().split())
R = map(int, input().split())
print("Yes") if sum(R)-H>=0 else print("No")
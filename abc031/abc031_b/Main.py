L,H = map(int,input().split())
record = [int(input())  for i in range(int(input()))]
print("\n".join([str(0) if L<=i<=H else str(-1) if i>H else str(L-i) for i in record]))
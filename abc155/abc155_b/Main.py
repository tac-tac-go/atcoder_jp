N = int(input())
A = list(map(int, input().split()))
R = [v for v in A if v % 2 == 0 and (v % 3 == 0 or v % 5 == 0)]
R2 = [v for v in A if v % 2 == 0]
print("APPROVED") if len(R)==len(R2) else print("DENIED")
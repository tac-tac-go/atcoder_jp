A,B = input().split()
A_sum = sum([int(i) for i in A])
B_sum = sum([int(i) for i in B])
print(max(A_sum,B_sum))
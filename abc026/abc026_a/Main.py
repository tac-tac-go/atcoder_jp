A = int(input())
num_list = [x*y for x in range(A) for y in range(A) if x+y==A]
print(max(num_list))
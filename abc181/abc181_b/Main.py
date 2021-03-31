N = int(input())
R = [map(int,input().split()) for i in range(N)]
sum_val = 0
for i1,i2 in R:
  sum_val+=(i1+i2)*(i2-i1+1)//2
print(sum_val)
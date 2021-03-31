X  = int(input())
sum_money =[(10000*(i+1))*(1/X) for i in range(X)]
print(int(sum(sum_money)))
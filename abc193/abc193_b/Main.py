N = int(input())
R = [map(int,input().split()) for i in range(N) ]
min_money =10**10
for a,p,x in R:
    if x-a>0:
        if min_money>p:min_money=p
print('-1') if min_money==10**10 else print(min_money)
  
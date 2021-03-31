x,y = map(int,input().split())
money=0
if x==1 and y==1:money+=400000
if x==1:money+=300000
if x==2:money+=200000
if x==3:money+=100000
if y==1:money+=300000
if y==2:money+=200000
if y==3:money+=100000
print(money)
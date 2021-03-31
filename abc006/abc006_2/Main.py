a=0;b=0;c=1
n = int(input())
if n==1:
    print(a)
    exit()
elif n==2:
    print(b)
    exit()
elif n==3:
    print(c)
    exit()

x=0
for i in range(3,n):
    x= a+b+c 
    x %= 10007
    a = b
    b = c
    c = x
    
print(x%10007)
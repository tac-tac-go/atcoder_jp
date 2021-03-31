a,b=map(int,input().split())

if  (type(a)==int) and( type(b)==int) and (-1000 <= a and 1000>=a ) and (-1000 <= b and 1000>=b ):
    print(max(a+b,a-b,a*b))
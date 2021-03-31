A,B,C = map(int,input().split())
from fractions import gcd
if C%gcd(A,B)==0:
    print("YES")
else:
    print("NO")
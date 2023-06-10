p,q = input().split()
y = [0,3,4,8,9,14,23]
i,j = y[ord(p)-ord("A")],y[ord(q)-ord("A")]
print(abs(i-j))

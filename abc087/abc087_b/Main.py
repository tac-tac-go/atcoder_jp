a,b,c,d = map(int,open(0))
print(sum(500*i+100*j+50*k==d for i in range(a+1) for j in range(b+1) for k in range(c+1)))
N=int(input())
v=sorted(map(int,input().split()))
value=v[0]
for i in range(1,N):
  value=(value+v[i])/2

print( int(value) if value%1==0 else value)
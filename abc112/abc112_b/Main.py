N,T = map(int,input().split())
record = [map(int,input().split()) for i in range(N)]
record2 = [i  for i,j in record if j<=T]
print(min(record2) if len(record2)!=0 else "TLE")
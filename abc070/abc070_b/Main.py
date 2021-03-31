A,B,C,D = map(int,input().split())
print(len(set(range(A+1,B+1)) & set(range(C+1,D+1))))
   
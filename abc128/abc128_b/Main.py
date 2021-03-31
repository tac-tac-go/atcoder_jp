N = int(input())
V = [input().split()+[i + 1] for i in range(N)]  
c_d = sorted(V,key=lambda x : (x[0],-int(x[1])))  
for v1 in c_d:
  print(v1[2])
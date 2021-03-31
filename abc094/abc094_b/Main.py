N,M,X = map(int,input().split())
A = list(map(int,input().split()))
mass_0 = [i for i in range(0,X+1) if i in A]
mass_N = [i for i in range(X,N) if i in A]
print(min(len(mass_0),len(mass_N)))
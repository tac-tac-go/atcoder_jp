i=input
N,K,X,Y = map(int,[i(),i(),i(),i()])
print(sum([X if i<K else Y for i in range(N)]))
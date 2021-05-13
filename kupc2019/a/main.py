n,x = map(int,input().split())
a = list(map(int,input().split()))
print(len([a_i for a_i in a if a_i+x>=max(a)]))
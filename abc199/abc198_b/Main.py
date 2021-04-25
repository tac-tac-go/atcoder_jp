n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
result = list(range(a[0],b[0]+1))
for i in range(1,len(a)):
    result = set(result)& set(list(range(a[i],b[i]+1)))
print(len(result))
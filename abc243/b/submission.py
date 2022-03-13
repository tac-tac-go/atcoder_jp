n = int(input())
an = list(map(int,input().split()))
bn = list(map(int,input().split()))
count1 = 0
for i,j in zip(an,bn):
  if i==j:
    count1+=1
print(count1)
print(len(list(set(an) & set(bn)))-count1)

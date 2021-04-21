n = int(input())
a,b = map(int,input().split())
k = int(input())
p = list(map(int,input().split()))
record = [0]*n
record[a-1]+=1
record[b-1]+=1
for p_i in p:
  record[p_i-1]+=1
print("YES") if max(record)<=1 else print("NO")
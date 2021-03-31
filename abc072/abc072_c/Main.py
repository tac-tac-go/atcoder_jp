n = int(input())
cnt = [0]*100002
a = list(map(int, input().split()))
for i in a:
  cnt[i]+=1
  cnt[i+1]+=1
  cnt[i+2]+=1
print(max(cnt))
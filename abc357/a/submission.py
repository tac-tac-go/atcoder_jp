N,M = map(int,input().split())
h_arr = list(map(int,input().split()))
count = 0
for i in h_arr:
  if M-i>=0:
    M-=i
    count+=1
  else:
    break
print(count)
    

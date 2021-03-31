N = int(input())
K = int(input())
score=1
for i in range(N):
  if score*2 <= score+K:score*=2
  else : score+=K
print(score)
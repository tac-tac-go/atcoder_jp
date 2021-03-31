N = int(input())
R = [2,1]
for i in range(N-1):
  R.append(R[-1]+R[-2])
print(R[-1])
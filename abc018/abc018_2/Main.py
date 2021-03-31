S = list(input())
N = int(input())
L = [list(map(int,input().split())) for i in range(N)]
for l1,l2 in L:
  S[l1-1:l2]="".join(S[l1-1:l2])[::-1]
print("".join(S))
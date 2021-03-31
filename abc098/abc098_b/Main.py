N = int(input())
S= input()
 
ans = 0
for i in range(N):
    s = set(S[:i]) & set(S[i:])
    ans=max(ans,len(s))
 
print(ans)
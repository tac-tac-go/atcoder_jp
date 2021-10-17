S = input()
mn = S
mx = S
for i in range(1, len(S)):
    T = S[i:] + S[:i]
    mn = min(mn, T)
    mx = max(mx, T)
print(mn)
print(mx)

S = input()
T = input()
diffs = [(26 + ord(t) - ord(s)) % 26 for s, t in zip(S, T)]
if all([d == diffs[0] for d in diffs]):
    print("Yes")
else:
    print("No")

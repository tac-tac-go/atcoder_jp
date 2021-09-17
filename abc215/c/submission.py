import itertools
s, k = input().split()
k = int(k)
s = list(s)
l = sorted(set(itertools.permutations(s, len(s))))
print("".join(l[k-1]))

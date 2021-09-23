import collections
s = list(input())
c = list(collections.Counter(s).values())
print("Yes") if len(set(c)) == 1 else print("No")

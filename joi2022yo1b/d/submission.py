from collections import Counter
n = int(input())
a = Counter(map(int, input().split()))
print(sorted(a.items(), key=lambda x: (x[1], x[0]))[0][0])

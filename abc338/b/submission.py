from collections import Counter
arr = Counter(list(input()))
print(sorted(arr.items(),key=lambda x:(-x[1],x[0]))[0][0])


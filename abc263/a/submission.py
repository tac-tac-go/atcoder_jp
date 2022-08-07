from collections import Counter
array = Counter(map(int,input().split()))
print("Yes") if sorted(array.values())==[2,3] else print("No")


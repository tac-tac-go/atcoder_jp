now = 0
a = int(input())
b = int(input())
count = 0
count += abs(a)
count += max(a,b) - min(a,b)
count += abs(b)
print(count)





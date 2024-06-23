n = int(input())
arr = [input() for i in range(n)]
print(sum([1 for i in arr if i=="Takahashi"]))

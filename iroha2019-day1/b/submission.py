s = input()
i = int(input())
divide = i%len(s)
print(s[divide:]+s[:divide])

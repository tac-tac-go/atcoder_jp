n = int(input())
an = list(map(int, input().split()))
print((((sum(an)*sum(an))-sum(map(lambda x: x**2, an)))//2) % (10**9+7))

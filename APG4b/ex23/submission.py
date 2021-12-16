from collections import Counter
n = int(input())
an = Counter(map(int,input().split()))
an = sorted(an.items(),key=lambda x:x[1],reverse=True)
print(an[0][0],an[0][1])

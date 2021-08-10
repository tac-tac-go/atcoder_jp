n = int(input())
an = list(map(int, input().split()))
an_sort = sorted(an)[::-1]
print(an.index(an_sort[1])+1)

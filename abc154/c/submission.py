n = int(input())
array = list(map(int,input().split()))
an = list(set(array))
print("YES") if len(an)==len(array) else print("NO")



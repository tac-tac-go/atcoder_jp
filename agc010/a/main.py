n = int(input())
a = sum(list(map(int,input().split())))
print("YES") if a%2==0 else print("NO")
s = input()
a,b = map(int,input().split())
s1 = s[a-1]
s2 = s[b-1]
print(s[:a-1]+s2+s[a:b-1]+s1+s[b:])

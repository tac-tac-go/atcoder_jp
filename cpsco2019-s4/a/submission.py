l,x = map(int,input().split())  
judge = x//l
print(x-l*judge) if judge%2==0 else print(l-(x-l*judge))

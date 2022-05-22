n,k = map(int,input().split())
an = list(map(int,input().split()))
bn = list(map(int,input().split()))
an_f = [i+1 for i,v in enumerate(an) if v==max(an)]
print("No") if len(list(set(an_f) & set(bn)))==0 else print("Yes")

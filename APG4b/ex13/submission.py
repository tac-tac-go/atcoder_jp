n = int(input())
an = list(map(int,input().split()))
average = int((sum(an)/len(an))//1)
for ai in an:
  print(abs(ai-average))




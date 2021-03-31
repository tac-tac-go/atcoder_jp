def resolve():
   N,S,T = map(int,input().split())
   W = [int(input()) for i in range(N)]
   total=0;count=0
   for w in W:
       total+=w
       if(S<=total<=T):count+=1
       
   print(count)
   
resolve()
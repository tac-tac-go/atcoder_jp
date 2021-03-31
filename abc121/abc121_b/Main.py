def resolve():
    N,M,C = map(int,input().split())
    *B, = map(int,input().split())
    count=0
    for i in range(N):
        A = map(int,input().split())
        if sum(map(lambda x,y:x*y,A,B))+C>0:
            count+=1
    print(count)

resolve()
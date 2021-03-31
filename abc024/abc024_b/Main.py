def resolve():
    N,T = map(int,input().split())
    A = [int(input()) for _ in range(N)]
    result=[]
    for i in range(N-1):
        if A[i]+T<=A[i+1]:
            result+=list(range(A[i],A[i]+T))
            
        else:
            result+=list(range(A[i],A[i+1]))
                  
    print(len(result)+T)

resolve()
def resolve():
    N,A,B = map(int,input().split())
    R = [input().split() for i in range(N)]
    score=0
    for v1,v2 in R:
        v2 = int(v2)
        if v2<A:
            if v1=="East":score+=A
            else:score-=A
        elif  A<=v2<=B:
            if v1=="East":score+=v2
            else:score-=v2
        else:
            if v1=="East":score+=B
            else:score-=B
    print("East",abs(score)) if score>0 else print("West",abs(score)) if score<0 else print(0)
            
resolve()   
        
    
    
        
        
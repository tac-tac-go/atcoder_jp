N = int(input())
R = [input().split() for i in range(N)]
X = input()
p_i = [i for i,(s,t) in enumerate(R) if s==X][0]
print(sum([int(v) for i,v in R[p_i+1:]]))
    
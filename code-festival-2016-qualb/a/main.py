s = list(input())
s2 = list("CODEFESTIVAL2016")
print(len([i for i,j in zip(s,s2) if i!=j]))

a = list(range(0,10))
b = list(map(int,list(input())))
print(list(set(a)-set(b))[0])

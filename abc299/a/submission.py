n = int(input())
s = input()
l_i = s.index("|")
r_i = s.rindex("|")
symbol = s.index("*")
print("in") if symbol>l_i and r_i > symbol else print("out")

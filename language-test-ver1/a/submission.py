n = int(input())
c = list(input())
c1 = c.count("1")
c2 = c.count("2")
c3 = c.count("3")
c4 = c.count("4")
print(max(c1, c2, c3, c4), min(c1, c2, c3, c4))

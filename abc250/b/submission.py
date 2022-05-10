n, a, b = (int(i) for i in input().split())

for t in range(n):
    for i in range(a) :
        white = True
        if (t+1) % 2 == 0 :
            white = False
        for l in range(n) :
            for j in range(b) :
                if white :
                    print(".", end = "")
                else :
                    print("#", end = "")
            white = not(white)
        print()

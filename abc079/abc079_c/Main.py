A, B, C, D = list(input())
Ai, Bi, Ci, Di = int(A), int(B), int(C), int(D)
if Ai + Bi + Ci + Di == 7:
    print(f'{Ai}+{Bi}+{Ci}+{Di}=7')
elif Ai + Bi + Ci - Di == 7:
    print(f'{Ai}+{Bi}+{Ci}-{Di}=7')
elif Ai + Bi - Ci + Di == 7:
    print(f'{Ai}+{Bi}-{Ci}+{Di}=7')
elif Ai + Bi - Ci - Di == 7:
    print(f'{Ai}+{Bi}-{Ci}-{Di}=7')
elif Ai - Bi + Ci + Di == 7:
    print(f'{Ai}-{Bi}+{Ci}+{Di}=7')
elif Ai - Bi + Ci - Di == 7:
    print(f'{Ai}-{Bi}+{Ci}-{Di}=7')
elif Ai - Bi - Ci + Di == 7:
    print(f'{Ai}-{Bi}-{Ci}+{Di}=7')
elif Ai - Bi - Ci - Di == 7:
    print(f'{Ai}-{Bi}-{Ci}-{Di}=7')
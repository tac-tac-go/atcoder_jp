p = [list(input()) for i in range(10)]
array = [0]*10
for p_r in p:
    for i, p_c in enumerate(p_r):
        if p_c == "o":
            array[i] += 1
print("Yes") if min(array) >= 1 else print("No")

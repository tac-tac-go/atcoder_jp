t = int(input())
s = [input() for i in range(t)]
for si in s:
    si_l = len(si)
    i = 0
    count = 0
    while i < si_l:
        if si[i:i+5] == "kyoto" or si[i:i+5] == "tokyo":
          i += 5
          count += 1
        else:
          i += 1
    print(count)

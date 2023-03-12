s = input()
print("".join([s[i+1]+s[i] for i in range(0,len(s),2)]))

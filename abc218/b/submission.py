alpha_l = list("abcdefghijklmnopqrstuvwxyz")
pl = list(map(int, input().split()))
print("".join([alpha_l[p-1] for p in pl]))

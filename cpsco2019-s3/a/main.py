s = input()
print("".join(['A' if s_i=="O" else 'O' if s_i=="A" else s_i for s_i in s ]))
import string
alpha_list = list(string.ascii_uppercase)*2
N = int(input())
S = input()
result=""
for s in S:
    result+=alpha_list[alpha_list.index(s)+N%26]
print(result)
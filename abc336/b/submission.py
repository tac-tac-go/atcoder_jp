import re
n = int(input())
print(len(list(re.search(r'0*$',f'{n:b}'))[0]))

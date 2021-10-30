from fractions import Fraction
def comb(n, k):
    if n < 0 or k < 0:
        pdt = 0
    else:
        pdt = 1
        for s in range(1, k + 1):
            pdt *= Fraction(n - s + 1, s)
    return pdt.numerator

n = int(input())
an = map(int, input().split())
import collections
l = collections.Counter(an)
n_c = comb(n, 2)
count = 0
for i, v in l.items():
    count += comb(v,2)
print(n_c-count)

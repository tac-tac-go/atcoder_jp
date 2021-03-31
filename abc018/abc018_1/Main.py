import numpy as np
S = list(map(int,[input(),input(),input()]))
S_copy = sorted(S.copy(),reverse=True)
[print(S_copy.index(s)+1) for s in S]
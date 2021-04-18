import numpy as np
c1 = np.array(list(input().split()))
c2 = np.array(list(input().split()))
c3 = np.array(list(input().split()))
c4 = np.array(list(input().split()))
c_1 = c4[::-1]
c_2 = c3[::-1]
c_3 = c2[::-1]
c_4 = c1[::-1]
print(" ".join(c_1))
print(" ".join(c_2))
print(" ".join(c_3))
print(" ".join(c_4))
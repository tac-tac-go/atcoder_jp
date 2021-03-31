import numpy as np
N,L = map(int, input().split())
apple_val = np.array([i for i in range(L,L+N)])
abs_apple_val = np.argmin(list(map(lambda x : abs(x),apple_val)))
print(sum(np.delete(apple_val,abs_apple_val)))
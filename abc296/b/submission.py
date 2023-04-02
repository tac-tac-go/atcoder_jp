import numpy as np
alpha = list("abcdefgh")
nums = list(range(1,9))[::-1]
array = np.array([list(input()) for i in range(8)])
index = np.where("*"==array)
print(alpha[index[1][0]]+str(nums[index[0][0]]))


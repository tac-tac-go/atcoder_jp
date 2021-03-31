import numpy as np
N = int(input())
T,A = map(int, input().split())
H = list(map(int, input().split()))
sub_l = np.array(list(map(lambda x :abs(((T-(x*0.006)))-A) ,H)))
print(np.argmin(sub_l)+1)
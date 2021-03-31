import math
def num_divisors_trial_division(n):
    num = 0
    for i in range(1, int(math.sqrt(n) + 1e-9) + 1):
        if n % i == 0:
            num += 1
            if n != i**2:
                num += 1
    
    return num

def resolve():
  N = int(input())
  print(len([i for i in range(1,N+1) if i%2==1 and num_divisors_trial_division(i)==8]))
  
resolve()
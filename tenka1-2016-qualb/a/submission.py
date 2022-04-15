import math 

fn = lambda x : math.floor((x**2 + 4.0)/8.0)

print(fn(fn(fn(20))))

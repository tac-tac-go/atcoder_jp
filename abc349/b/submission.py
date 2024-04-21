from collections import Counter,defaultdict
s_arr = Counter(list(input()))
d = defaultdict(int)
for index,(key,value) in enumerate(s_arr.items()):
  d[value-1]+=1
flag = all(i==0 or i==2 for i in d.values())
print("Yes") if flag else print("No")
    
  

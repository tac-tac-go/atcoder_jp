N,M = map(int,input().split())
c_arr = input().split()
d_arr = input().split()
p_arr = list(map(int,input().split()))
p_rest = p_arr[0]
p_arr = p_arr[1:]
dic = dict(zip(d_arr,p_arr))
print(sum([dic.get(i,p_rest) for i in c_arr]))
  

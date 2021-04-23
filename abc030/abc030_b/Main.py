n,m = map(int,input().split())
n = n%12
n_r = (n%12)*30+(m/60)*30
m_r = (m/60)*360
a = max(n_r,m_r)-min(n_r,m_r)
b = (360-max(n_r,m_r))+min(n_r,m_r)
print(min(a,b))
x,y,z = map(int,input().split())
l_r = int(z*(y/x))
for i in range(l_r+5,l_r-5,-1):
  if i/z<y/x:
    print(int(i))
    break
def resolve():
    m = int(input())
    vv = m/1000
    if vv<0.1:vv = 0
    elif 0.1 <= vv <=5:vv = vv*10
    elif 6<= vv <= 30 : vv=vv+50
    elif 35<=vv<=70:vv=((vv-30)/5)+80
    else: vv = 89         
    print("{:02d}".format(int(vv)))
resolve()
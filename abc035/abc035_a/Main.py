W,H = map(int,input().split())
print("16:9") if W%16==0 and H%9==0 else print("4:3")
a,b = map(int,input().split())
result=[]
value=1
diff = b-a
result=[i+1 for i in range(0,diff)]
print(sum(result)-b)
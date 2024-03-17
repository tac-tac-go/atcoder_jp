_ = int(input())
s = input()
result = [0,0,0]
for i,v in enumerate(s):
 if v=="A":
   result[0]+=1
 elif v=="B":
   result[1]+=1
 else:
   result[2]+=1
 if all(result):
    print(i+1)
    break
     

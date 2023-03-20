alpha = list("abcdefghijklmnopqrstuvwxyz".upper())
h,w = map(int,input().split())
array = [list(map(int,input().split())) for i in range(h)]
result = ""
for i in array:
  for j in i:
    if j==0:
      result+="."
    else:
      result+=alpha[j-1]
  result+="\n"
print(result)
    
    

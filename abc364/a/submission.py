import sys
n = int(input())
arr = [input() for i in range(n)]
flag = False
for i in range(0,len(arr)-2):
  if arr[i]=="sweet" and arr[i]==arr[i+1]:
    flag = True
    break
print("No") if flag else print("Yes")

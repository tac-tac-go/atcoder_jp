arr = list(map(int,input().split()))
import sys
if arr == sorted(arr):
  if len(list(filter(lambda x : x>=100 and x<=675,arr)))==len(arr):
    if len(list(filter(lambda x : x%25==0,arr)))==len(arr):
           print("Yes")
           sys.exit(0)
print("No")
       
           

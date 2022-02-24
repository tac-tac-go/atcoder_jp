from collections import Counter
import numpy as np
array = list(input())
count = [0,0,0,0]#n0,s1,w2,e3
for i in array:
  if i=="N":count[0]+=1
  elif i=="W":count[2]+=1
  elif i=="S":count[1]+=1
  else:count[3]+=1
judge1=np.array(count[0:2])
judge2=np.array(count[2:])
jugge1_b = False
jugge2_b = False

if np.all(judge1==0)==True:
  jugge1_b = True
else:
  if min(judge1)!=0:
    jugge1_b = True

if np.all(judge2==0)==True:
  jugge2_b = True
else:
  if min(judge2)!=0:
    jugge2_b = True

if jugge1_b and jugge2_b:print("Yes")
else:print("No")

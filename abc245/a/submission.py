import datetime
a,b,c,d = map(int,input().split())
time1 = datetime.timedelta(hours=a,minutes=b)
time2 = datetime.timedelta(hours=c,minutes=d,seconds=1)
if time1 > time2:
  print("Aoki")
else:
  print("Takahashi")



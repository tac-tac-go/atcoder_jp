k = int(input())
time = 60*21
time +=k
div,mod = divmod(time,60)
print("{:02d}:{:02d}".format(div,mod))

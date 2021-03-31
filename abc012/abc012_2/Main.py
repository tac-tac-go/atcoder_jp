N = int(input())
hour = int(N/3600)
minutes = int((N-(hour*3600))/60)
second = (N-(hour*3600+minutes*60))
print('{:02}:{:02}:{:02}'.format(hour,minutes,second))
        
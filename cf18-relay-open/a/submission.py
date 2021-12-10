days= ['Mon','Tue','Wed','Thu','Fri','Sat','Sun','Mon']
count = int(input())
for i in range(count):
  value = input()
  print(days[days.index(value)+1])


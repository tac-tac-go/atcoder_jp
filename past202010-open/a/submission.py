a, b, c = map(int, input().split())
if a > b > c:
  print("B")
elif a > c > b:
  print("C")
elif b > a > c:
  print("A")
elif b > c > a:
  print("C")
elif c > a > b:
  print("A")
else:
  print("B")

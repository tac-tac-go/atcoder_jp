a, b = map(int, input().split())
for i in range(0, 256):
    if bin(a ^ i) == bin(b):
      print(i)
      break

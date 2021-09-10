import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """9"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """119"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10000000"""
        output = """24"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  import math
  P = int(input())
  count = 0
  for i in range(10, 0, -1):
    X = math.factorial(i)
    while P >= X:
      P -= X
      count += 1
  print(count)
  



  # while p>0:
  #   c = list(map(lambda x:x-p,a))
  #   print()

  # a = [math.factorial(i) for i in range(1,101)]
  
  
  # b = [100]*100
  # while p>0:
    



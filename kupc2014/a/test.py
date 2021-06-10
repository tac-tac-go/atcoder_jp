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
        input = """1 2 3 4 5 6"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 2 3 2 4 0"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  import numpy as np
  ab = list(map(int,input().split()))
  a = ab[:3]
  a.sort()
  b = ab[3:]
  b.sort()
  score=0
  for i in a:
    min_index = np.argmin(map(lambda x:abs(x-i),b))
    score+=abs(i-b[min_index])
    b.pop(min_index)
  print(score)


    


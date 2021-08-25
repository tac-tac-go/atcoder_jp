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
        input = """2018 2"""
        output = """2100"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """888 0"""
        output = """889"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 7"""
        output = """10000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  import math
  x,k = map(int,input().split())
  min_val = int("1"+("0")*k)
  if min_val >=x+1:
    print(min_val)
  else:
    print((math.ceil((x+1)/min_val))*min_val)

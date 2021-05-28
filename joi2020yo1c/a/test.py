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
        input = """8 3 6"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 3 10"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8 10 10"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  import numpy as np
  x,l,r = map(int,input().split())
  l_r = list(range(l,r+1))
  print(l_r[np.argmin(list((map(lambda li:abs(x-li),l_r))))])
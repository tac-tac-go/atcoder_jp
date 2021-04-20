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

    def test_入力例1(self):
        input = """4
ooxx
xoox
xxxx
xxxx"""
        output = """xxxo
xxoo
xxox
xxxx"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  import numpy as np
  n = int(input())
  s = np.array([list(input()) for i in range(n)])
  for i in range(n):
    print("".join(s[:,i][::-1]))
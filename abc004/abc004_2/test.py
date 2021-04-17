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
        input = """. . . .
. o o .
. x x .
. . . ."""
        output = """. . . .
. x x .
. o o .
. . . ."""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """o o x x
o o x x
x x o o
x x o o"""
        output = """o o x x
o o x x
x x o o
x x o o"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  import numpy as np
  c1 = np.array(list(input().split()))
  c2 = np.array(list(input().split()))
  c3 = np.array(list(input().split()))
  c4 = np.array(list(input().split()))

  c_1 = c4[::-1]
  c_2 = c3[::-1]
  c_3 = c2[::-1]
  c_4 = c1[::-1]

  print(" ".join(c_1))
  print(" ".join(c_2))
  print(" ".join(c_3))
  print(" ".join(c_4))
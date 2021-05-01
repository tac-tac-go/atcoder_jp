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
        input = """15 10
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snuke snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake
snake snake snake snake snake snake snake snake snake snake"""
        output = """H6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1
snuke"""
        output = """A1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  import string
  import numpy as np
  h,w = map(int,input().split())
  col = list(string.ascii_uppercase)
  row = list(range(1,h+1))
  array = np.array([input().split() for i in range(h)])
  for i in range(h):
    for j in range(w):
      if array[i,j]=="snuke":
        print(str(col[j])+str(row[i]))
        break
  
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
        input = """E 120
E 90"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """W 165
E 165"""
        output = """22"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  c1, a = input().split()
  c2, b = input().split()
  a = int(a)
  b = int(b)
  print((abs(a-b))//15) if c1 == c2 else print((a+b)//15)

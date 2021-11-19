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
        input = """314 2"""
        output = """693"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000000000 100"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6174 100000"""
        output = """6174"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n,k = map(int,input().split())
  a = n
  for i in range(k):
    g1 = "".join(sorted(list(str(a)),reverse=True))
    g2 = g1[::-1]
    g1 = int(g1)
    g2 = int(g2)
    a = g1 - g2
  print(a)


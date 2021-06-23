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
        input = """100 40 35"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100 60 70"""
        output = """30"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """14000000 2458 692196"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
  n,a,b = map(int,input().split())
  print(0) if n>a+b else print((a+b)-n)
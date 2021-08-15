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
        input = """214"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """126"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  print(4) if 1<=n<=125 else print(6) if 126<=n<=211 else print(8)
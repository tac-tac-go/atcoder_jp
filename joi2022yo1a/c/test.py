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
        input = """4
BABE"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
DAD"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
BACED"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """28
EEEEEEEEEEEEEEEEEEEEEEEEEEEE"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  s = set(list(input()))
  print("Yes") if len(s)>=3 else print("No")

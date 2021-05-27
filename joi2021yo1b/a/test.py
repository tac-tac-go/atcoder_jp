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
        input = """2 5 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 22 19"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """24 30 30"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1 100 99"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  a,b,c = map(int,input().split())
  print(1) if a<=c<b else print(0)
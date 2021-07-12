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
        input = """SAINT HELENA"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """SOUND HOUND"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """SOUND SPIDER"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """S H"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """X Y"""
        output = """NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  x, y = input().split()
  print("YES") if x[0]=="S" and y[0]=="H" else print("NO")
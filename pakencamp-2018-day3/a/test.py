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
        input = """2018 12 25"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2018 12 24"""
        output = """NOT CHRISTMAS DAY"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2234 12 25"""
        output = """216"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  y,m,d = map(int,input().split())
  print(y-2018) if m==12 and d==25 else print("NOT CHRISTMAS DAY")
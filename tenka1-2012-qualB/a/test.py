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
        input = """2 3 2"""
        output = """23"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1 1"""
        output = """1
106"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 4 6"""
        output = """104"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  a,b,c = map(int,input().split())
  for i in range(1,128):
    if i%3==a and i%5==b and i%7==c:
      print(i)
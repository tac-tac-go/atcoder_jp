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
        input = """1
80
5"""
        output = """400"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """2
umai
150
3"""
        output = """umai!
450"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """2
good!
30
8"""
        output = """good!!
240"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  if n==1:
    price = int(input())
    N = int(input())
    print(price*N)
  else:
    text = input()
    price = int(input())
    N = int(input())
    print(text+"!")
    print(price*N)

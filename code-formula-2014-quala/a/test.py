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
        input = """8"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """24"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """27"""
        output = """YES"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  a = int(input())
  flag = False
  for i in range(1, 101):
    if i**3 == a:
        flag = True
        break
  print("YES") if flag else print("NO")


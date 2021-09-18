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
        input = """2021"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2015"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5947"""
        output = """3932"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  N = int(input())
  if N == 2015:
      print(1)
  elif N == 2016:
      print(2)
  elif N >= 2018:
      print(N - 2015)
  else:
      print(-1)

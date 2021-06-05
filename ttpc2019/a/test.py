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
        input = """2015 2019 2020"""
        output = """2023"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2015 2019 2027"""
        output = """2027"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000 2999 3000"""
        output = """4998"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  a,b,t = map(int,input().split())
  start = a
  while start<t:
    start+=b-a
  print(start)
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
        input = """4 50
80 60 40 0"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 90
89 89 89"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 22
6 37"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
  n,p = map(int,input().split())
  an = map(int,input().split())
  print(len([i for i in an if i<p]))


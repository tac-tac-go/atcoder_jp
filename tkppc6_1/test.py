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
        input = """6 2
1 1 1 2 4 4"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 0
0 1 2 3 4 5 6"""
        output = """7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n,m = map(int,input().split())
  an = map(int,input().split())
  print(min(len(set(an))+m,n))
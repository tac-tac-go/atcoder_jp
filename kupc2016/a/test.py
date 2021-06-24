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
        input = """5 5 9
4
3
6
9
1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5 4 9
5
6
7
8
9"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """4 3 6
9
6
8
1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """2 1 2
1
2"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n,a,b = map(int,input().split())
  t = [int(input()) for i in range(n)]
  count=0
  for ti in t:
    if not(ti>=a and ti<b):count+=1
  print(count)
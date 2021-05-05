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
        input = """5
1 1 2 2 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 2 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
1 1 1 1 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """14
1 2 2 3 3 3 4 4 4 4 1 2 3 4"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  from itertools import groupby
  n = int(input())
  a = list(map(int,input().split()))
  ans =0
  for (key,group) in groupby(a):
    ans += len(list(group))//2
  print(ans)



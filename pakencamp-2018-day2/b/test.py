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
        input = """4 2
20 18 12 24"""
        output = """32"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 5
8 6 9 1 20"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 8
1268 1755 2315 1071 1229 1101"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """8 3
1345 1355 1390 1285 1171 936 1272 855"""
        output = """2516"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n, d = map(int, input().split())
  l = sorted(map(int, input().split()), reverse=True)
  ans = 0
  m = n//d
  for i in range(m):
      ans += min(l[d*i:d*(i+1)])
  print(ans)

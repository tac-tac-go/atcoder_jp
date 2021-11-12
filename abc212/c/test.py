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
        input = """2 2
1 6
4 9"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1
10
10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 8
82 76 82 82 71 70
17 39 67 2 45 35 22 24"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  from bisect import bisect_right
  INF = 10**11
  n,m = map(int,input().split())
  a = list(map(int,input().split()))
  b = list(map(int,input().split()))+[-INF,INF]  
  a.sort()
  b.sort()
  ans = 10**10
  for x in a:
    pos = bisect_right(b,x)
    ans = min(ans,abs(b[pos]-x))
    ans = min(ans,abs(b[pos-1]-x))
  print(ans)


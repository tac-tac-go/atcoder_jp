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
        input = """6
2 4 4 9 4 9"""
        output = """20"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
200 4 4 9 4 9"""
        output = """200"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  an = list(map(int,input().split()))
  ans=-9999
  for i in range(n):

    mi = an[i]
    ans = max(an[i],ans)

    for j in range(i,n):
      mi = min(mi,an[j])
      ans = max(ans,mi*(j-i+1))
  print(ans)

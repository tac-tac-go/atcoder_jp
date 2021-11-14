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
        input = """3
10 20 39"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
666 777 888 777 666"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  N = int(input())
  S = list(map(int, input().split()))
  ans = 0
  for s in S:
    flag = False
    for a in range(1, 333):
      for b in range(1, 333):
        if 4*a*b+3*a+3*b == s:
          flag = True
    if not flag:
      ans += 1

  print(ans)


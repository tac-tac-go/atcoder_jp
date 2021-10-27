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
        input = """35"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """369"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6227384"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """11"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = input()
  cnt = [0] * 3
  for c in n:
      d = ord(c) - ord('0')
      cnt[d % 3] += 1

  now = (cnt[1] + cnt[2] * 2) % 3

  def solve():
      if now == 0:return (0)
      elif now == 1:
          if cnt[1] >= 1:return (1)
          elif cnt[2] >= 2:return (2)
      else:
          if cnt[2] >= 1:return (1)
          elif cnt[1] >= 2:return (2)

  ans = solve()

  if ans == len(n):
      print(-1)
  else:
      print(ans)
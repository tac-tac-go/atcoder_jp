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
        input = """2
abcd
efgh"""
        output = """abcdefgh"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
caa
abb
ab"""
        output = """ababb"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()


def resolve():
  n = int(input())
  a = [input() for _ in range(n)]
  b = []
  for i in range(n):
    for j in range(n):
      if i != j:
        b.append(a[i]+a[j])
  b.sort()
  print(b[0])

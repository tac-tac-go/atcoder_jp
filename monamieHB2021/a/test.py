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
        input = """44"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """52"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  ans = 100
  for a in range(26):
      for b in range(26):
          if (n - (8 * a + 10 * b)) % 26 == 0:
              ans = min(ans, a + b)
  print(ans)

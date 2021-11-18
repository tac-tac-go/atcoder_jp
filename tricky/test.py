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

    def test_入力例(self):
        input = """3
10 11
10 10
-3 -2"""
        output = """0
1
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  N = int(input())
  for i in range(N):
      A, B = map(int, input().split())
      ans = abs(A) // abs(B)
      if A * B > 0:
          print(ans)
      else:
          print(-ans)

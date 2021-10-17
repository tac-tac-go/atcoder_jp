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
        input = """aaba"""
        output = """aaab
baaa"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """z"""
        output = """z
z"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """abracadabra"""
        output = """aabracadabr
racadabraab"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  S = input()
  mn = S
  mx = S
  for i in range(1, len(S)):
      T = S[i:] + S[:i]
      mn = min(mn, T)
      mx = max(mx, T)
  print(mn)
  print(mx)

    


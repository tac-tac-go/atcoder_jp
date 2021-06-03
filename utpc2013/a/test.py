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
        input = """KUPC"""
        output = """yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """UTPC"""
        output = """yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """UTBC"""
        output = """no"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  o_0 = list('CEFGHIJKLMNSTUVWXYZ')
  o_1 = list('ADOPQR')
  s = list(input())
  if s[0] in o_0 and s[1] in o_0 and s[2] in o_1 and s[3] in o_0:
    print("yes")
  else:
    print("no")
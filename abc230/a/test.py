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
        input = """42"""
        output = """AGC043"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """19"""
        output = """AGC019"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1"""
        output = """AGC001"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """50"""
        output = """AGC051"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  if n>=42:
    print("AGC{:03d}".format(n+1))
  else:
    print("AGC{:03d}".format(n))

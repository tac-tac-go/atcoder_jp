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
        input = """ARC
AGC
AHC"""
        output = """ABC"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """AGC
ABC
ARC"""
        output = """AHC"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  s1 = input()
  s2 = input()
  s3 = input()
  print(set(["ABC","ARC","AGC","AHC"])-set([s1,s2,s3])))
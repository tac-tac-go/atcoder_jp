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

    def test_入力例1(self):
        input = """12B34567"""
        output = """Bachelor 12"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """00M00000"""
        output = """Master 00"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """13D10007"""
        output = """Doctor 13"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  s = input()
  y = s[:2]
  g = s[2]
  if g == "B":
    print("Bachelor",y)
  elif g == "M":
    print("Master",y)
  else:
    print("Doctor",y)
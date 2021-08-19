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
        input = """100 40"""
        output = """Congratulations!"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """0 100"""
        output = """Enjoy another semester..."""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """60 60"""
        output = """Congratulations!"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  a,s = map(int,input().split())
  print("Congratulations!") if a >= s else print("Enjoy another semester...")

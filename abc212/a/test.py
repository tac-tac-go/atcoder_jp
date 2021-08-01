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
        input = """50 50"""
        output = """Alloy"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100 0"""
        output = """Gold"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0 100"""
        output = """Silver"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """100 2"""
        output = """Alloy"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  a,b = map(int,input().split())
  print("Gold") if a > 0 and b == 0 else print(
      "Silver") if a == 0 and b > 0 else print("Alloy")

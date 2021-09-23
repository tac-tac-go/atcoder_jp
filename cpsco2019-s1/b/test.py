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
        input = """ababcc"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """reiwa"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """cpsco"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  s = list(input())
  import collections
  c = list(collections.Counter(s).values())
  print("Yes") if len(set(c))==1 else print("No")


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
        input = """oohay"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """abcde"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """yahoo"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """yohaa"""
        output = """NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  s = list(input())
  s2 = list("yahoo")
  s.sort()
  s2.sort()
  print("YES") if "".join(s) == "".join(s2) else print("NO")

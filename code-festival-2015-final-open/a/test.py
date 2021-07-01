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
        input = """using namespace std"""
        output = """invalid"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """using namespa cestd"""
        output = """valid"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  s,t,u = input().split()
  print("valid") if len(s)==5 and len(t)==7 and len(u)==5 else print("invalid")
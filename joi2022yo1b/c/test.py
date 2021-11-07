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
        input = """6
IOJOIJ"""
        output = """O
I"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
JJOI"""
        output = """J"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
IOJOJOJ"""
        output = """O
O
O"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5
JJJJJ"""
        output = """J
J
J
J"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  s = input()
  for i in range(n-1):
    if s[i+1]=="J":print(s[i])
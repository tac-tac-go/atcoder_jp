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
        input = """0 2 4
1"""
        output = """1 0 0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4 8
10"""
        output = """7 16 22"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  a,b,c = map(int,input().split())
  n = int(input())
  print(max(n-a,0),max((2*n)-b,0),max((3*n)-c,0))
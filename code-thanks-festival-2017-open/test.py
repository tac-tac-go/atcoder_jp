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
        input = """240
600
1800
3600
4800
7200
10000
0"""
        output = """10000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10400
10300
10100
9800
9500
8500
7000
5000"""
        output = """10400"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0
0
0
0
0
0
0
0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  a = [int(input()) for i in range(8)]
  print(max(a))
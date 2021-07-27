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
        input = """79
6"""
        output = """78"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100
100"""
        output = """100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """43
5"""
        output = """40"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """56
1"""
        output = """56"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  a = int(input())
  b = int(input())
  for i in range(a,0,-1):
    if i%b==0:print(i);break
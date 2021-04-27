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
        input = """100 200 100"""
        output = """199"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """103 971 593"""
        output = """5590"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000 1 1"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  x,y,z = map(int,input().split())
  l_r = int(z*(y/x))
  for i in range(l_r+5,l_r-5,-1):
    if i/z<y/x:
      print(int(i))
      break

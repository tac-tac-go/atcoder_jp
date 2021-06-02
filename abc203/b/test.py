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
        input = """1 2"""
        output = """203"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3"""
        output = """1818"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n,k = map(int,input().split())
  print(["{}0{}".format(i,j) for i in range(1,n+1) for j in range(1,k+1)])
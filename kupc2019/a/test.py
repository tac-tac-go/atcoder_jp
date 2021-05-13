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
        input = """5 5
1 3 5 7 9"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2
1 3 5 7 9"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n,x = map(int,input().split())
  a = list(map(int,input().split()))
  print(len([a_i for a_i in a if a_i+x>=max(a)]))
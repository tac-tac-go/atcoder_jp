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
        input = """6 4
9
7
1
1
9
8"""
        output = """37"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 5
0
5
7
8
7
0
9
3"""
        output = """42"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n,k = map(int,input().split())
  an = sorted([int(input()) for i in range(n)])[::-1]
  print(sum(an[:k])+sum(map(lambda x:x*2,an[k:])))

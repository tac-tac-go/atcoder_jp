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
        input = """3
2 1 4
2
1 1
2 3"""
        output = """6
9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
7 2 3 8 5
3
4 2
1 7
4 13"""
        output = """19
25
30"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  t = list(map(int,input().split()))
  m = int(input())
  px = [map(int,input().split()) for i in range(m)]
  for p,x in px:
    t_c = t.copy()
    t_c[p-1]=x
    print(sum(t_c))



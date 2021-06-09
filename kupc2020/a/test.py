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
1 2
2 3
4 6"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
0 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
-2 3
1 4
5 2
4 -2"""
        output = """15"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  xy = [list(map(int,input().split())) for i in range(n)]
  result=0
  for i in range(1,len(xy)):
    result+=abs(xy[i][0]-xy[i-1][0])+abs(xy[i][1]-xy[i-1][1])
  print(result)
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
        input = """5
1
2
3
4
5"""
        output = """100000
50000
30000
20000
10000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8
8
7
6
5
4
3
2
1"""
        output = """0
0
0
10000
20000
30000
50000
100000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
1
5
4
2
7
6
3"""
        output = """100000
20000
0
30000
50000
0
10000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()


def resolve():
  n = int(input())
  award = [100000, 50000, 30000, 20000, 10000]
  id = [int(input()) for i in range(n)]
  for i in id:
    if (i-1)<5:
      print(award[i-1])
    else:
      print(0)

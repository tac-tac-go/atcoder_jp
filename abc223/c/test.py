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
1 1
2 1
3 1"""
        output = """3.000000000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 3
2 2
3 1"""
        output = """3.833333333333333"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
3 9
1 2
4 6
1 5
5 3"""
        output = """8.916666666666668"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  N = int(input())
  AB = [tuple(map(int,input().split())) for _ in range(N)]
  s = sum([A/B for A,B in AB])/2
  length=0
  for A,B in AB:
    if A/B <= s:
      s-=A/B
      length+=A
    else:
      length+=s*B
      break
  print(length)



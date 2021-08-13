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
        input = """5 17
4 5 7 9 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 9
3 6"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 9
1 2 3 4 5 6 7 8 9 10"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 129
12 42 13 25 32 19 14 9 21 12"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n,m = map(int,input().split())
  an = list(sorted(map(int,input().split())))[::-1]
  kind = 0
  for i in an:
      if m<=0:break
      else:
          m-=i
          kind+=1
  print(kind)

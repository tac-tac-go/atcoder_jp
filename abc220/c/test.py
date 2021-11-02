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
3 5 2
26"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
12 34 56 78
1000"""
        output = """23"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  an = list(map(int,input().split()))
  x = int(input())
  an_s = sum(an)
  count = x//an_s
  result = count*len(an)
  rest = x - (an_s)*count
  for i,v in enumerate(an):
    if rest < 0:
      break
    else:
      rest-=v
      result+=1
  print(result)

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
        input = """-10
20
5
10
3"""
        output = """120"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """35
92
31
50
11"""
        output = """627"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  a = int(input())
  b = int(input())
  c = int(input())
  d = int(input())
  e = int(input())
  if a<0:
    print(abs(a*c)+d+abs(b*e))
  elif a==0:
    print(d+(b*e))
  else:
    print((b-a)*e)


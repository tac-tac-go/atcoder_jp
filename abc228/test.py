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
        input = """7 20 12"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 7 12"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """23 0 23"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  s,t,x = map(int,input().split())
  seach = []
  if s<t:
    search = list(range(s,t+1))
  else:
    search = list(range(24,s-1,-1))+list(range(1,t+1,1))
  if x in search:
    print("Yes")
  else:
    print("No")
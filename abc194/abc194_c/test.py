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
2 8 4"""
        output = """56"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
-5 8 9 -4 -3"""
        output = """950"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  N = int(input())
  A = list(map(int,input().split()))
  sum_c = 0
  for i in range(1,N):
    for j in range(0,i):
        sum_c+=(A[i]-A[j])**2
  print(sum_c)
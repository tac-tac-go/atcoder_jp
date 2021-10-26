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
        input = """8 3
ACACTACG
3 7
2 3
1 8"""
        output = """2
0
3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  import itertools
  N, Q = map(int, input().split())
  S = input()
  AC = [0] * (N)
  for i in range(1, N):
    if S[i-1] == 'A' and S[i] == 'C':
      AC[i] = 1
  SAC = [0] + list(itertools.accumulate(AC))
  for i in range(Q):
    l,r = map(int,input().split())
    print(SAC[r]-SAC[l])

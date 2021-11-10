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
3 0
5 1 1
7 1 1"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1000000000 0
1000000000 0
1000000000 0
1000000000 0
1000000000 4 1 2 3 4"""
        output = """5000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  t = [0] * (n+1)
  k = [0] * (n+1)
  a = [0] * (n+1)

  for i in range(1,n+1):
    inp = list(map(int,input().split()))
    t[i] = inp[0]
    k[i] = inp[1]
    a[i] = inp[2:]
  
  need = [False] * (n+1)
  need[n] = True

  for i in range(n,0,-1):
    if not need[i]:
      continue
    for child in a[i]:
      need[child] = True
  print(sum(t[i] for i in range(1,n+1) if need[i]))
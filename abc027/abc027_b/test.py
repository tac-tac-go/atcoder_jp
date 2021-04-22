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

    def test_入力例1(self):
        input = """3
1 2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5
2 0 0 0 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """2
0 99"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """4
0 0 0 0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  import itertools
  n = int(input())
  a = list(map(int,input().split()))
  if sum(a)%n!=0:
    print("-1")
  else:
    ave = sum(a)//n
    ans = 0
    a_c = list(itertools.accumulate(a))
    for i in range(n-1):
      if a_c[i]!=ave*(i+1):
        ans+=1
    print(ans)


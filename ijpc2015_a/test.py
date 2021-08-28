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
2 3 2"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5
6 6 9 7 4"""
        output = """46"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """10
10 6 6 10 3 8 8 9 4 2"""
        output = """86"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  a = sorted(map(int,input().split()))
  count=0
  for i in range(n-1):
    count+=max(a[i],a[i+1])
  count+=a[0]
  count+=a[-1]
  count+=n
  print(count)

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
        input = """2 7
1 8"""
        output = """4
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 3
33"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7 1000000000000
99 8 2 4 43 5 3"""
        output = """142857142857
142857142857
142857142858
142857142857
142857142857
142857142857
142857142857"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n,k = map(int,input().split())
  an = list(map(int,input().split()))
  bn = sorted(an)
  q,mod = divmod(k,n)
  result={}
  for i in bn:
    result[i]=q
  for i in range(0,mod,1):
    result[bn[i]]+=1
  for i in an:
    print(result[i])
    

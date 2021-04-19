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
5 8 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """9
1 2 3 4 5 6 7 8 9"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  a = list(map(int,input().split()))
  count=0
  for a_i in a:
    while a_i%2==0 or (a_i-2)%3==0:
      a_i-=1
      count+=1  
  print(count)
    


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
        input = """3 1
3 10"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 10
3 10"""
        output = """29"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  ma,da = map(int,input().split())
  mb,db = map(int,input().split())
  month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if ma==mb:print(db-da) 
  else:
    count=0
    print(sum([month[i-1] for i in range(ma,mb,1)])-da+db)
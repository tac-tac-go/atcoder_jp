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
        input = """5
3 1 2 4 5"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
3 1 4 1 5 2"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
1 2 3"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1
1"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  a = list(map(int,input().split()))
  print("Yes") if len(set(list(range(1,n+1)))-set(a))==0 else print("No")
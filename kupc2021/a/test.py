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
1 2 5
3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1 1 1 1 1
2021"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
623690081 433933447 476190629 262703497 211047202 971407775 628894325 731963982 822804784 450968417
128512451"""
        output = """7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  s = list(map(int,input().split()))
  t = int(input())
  result = set(map(lambda x : x//t,s))
  print(len(result))
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
        input = """4
2 1 2
2 1 1
2 2 1
2 1 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1 1
1 1
1 2
2 1 1
3 1 1 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
1 1"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  la = [input().split() for i in range(n)]
  result = []
  for la_i in la:
    l = la_i[0]
    a = ','.join(la_i[1:])
    result.append(a)
  from collections import Counter
  print(len(Counter(result)))

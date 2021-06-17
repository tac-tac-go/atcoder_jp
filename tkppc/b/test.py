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
        input = """2
123
146"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4
124
23
145
145"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """10
41
467
334
0
169
224
478
358
462
464"""
        output = """7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  a = [int(input()) for i in range(n)]
  print(a.index(max(a))+1)
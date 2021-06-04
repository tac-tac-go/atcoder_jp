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

    def test_Sample_Input_1(self):
        input = """3
2 3 5"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10
1 1 1 1 1 1 1 1 1 1"""
        output = """11"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  import itertools
  n = int(input())
  p = list(map(int,input().split()))
  print(len(set([sum(v) for i in range(0,n+1) for v in itertools.combinations(p,i)])))

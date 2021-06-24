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
        input = """5
3 1 5 4 2"""
        output = """15"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
1 2 3 4 5 6"""
        output = """21"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7
7 6 5 4 3 2 1"""
        output = """28"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """20
19 11 10 7 8 9 17 18 20 4 3 15 16 1 5 14 6 2 13 12"""
        output = """210"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  l = list(map(int,input().split()))
  print(sum(l))
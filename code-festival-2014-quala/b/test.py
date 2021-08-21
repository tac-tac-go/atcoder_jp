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
        input = """abc
7"""
        output = """a"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """bbb
9"""
        output = """b"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """kljhasdfkjahfadfakhsdfaklh
1000000000"""
        output = """h"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  a = list(input())
  b = int(input())
  print(a[b%len(a)-1])

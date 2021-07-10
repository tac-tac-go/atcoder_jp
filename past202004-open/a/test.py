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
        input = """1F 5F"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """B1 B7"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1F B1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """B9 9F"""
        output = """17"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  st_list = "B9,B8,B7,B6,B5,B4,B3,B2,B1,1F,2F,3F,4F,5F,6F,7F,8F,9F".split(",")
  s,t = input().split()
  print(abs(st_list.index(s)-st_list.index(t)))

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
        input = """4 8
colopl"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 7
kitayuta"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7 8
kyuri"""
        output = """NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  a,b = map(int,input().split())
  s = input()
  print("YES") if a<=len(s) and len(s)<=b else print("NO")
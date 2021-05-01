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
        input = """C0DEFESTIVAL2O16"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """FESTIVAL2016CODE"""
        output = """16"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  s = list(input())
  s2 = list("CODEFESTIVAL2016")
  print(len([i for i,j in zip(s,s2) if i!=j]))

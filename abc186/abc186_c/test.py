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
        input = """20"""
        output = """17"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100000"""
        output = """30555"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  oct_v = [i for i in range(1,n+1) if "7" in oct(i)]
  ten_v = [i for i in range(1,n+1) if "7" in str(i)]
  print(n-len(set(oct_v+ten_v)))
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
        input = """33"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1333"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10000000"""
        output = """999"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  N = int(input())
  for i in range(1, 1000001):
    if int(str(i) * 2) > N:
        print(i - 1)
        exit()
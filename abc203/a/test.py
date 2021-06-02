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
        input = """2 5 2"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 5 6"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 1 1"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  abc_b = list(input().split())
  abc = list(set(abc_b))
  if len(abc)==3:
    print(0)
  else:
    if abc_b[0]==abc_b[1]:
      print(abc_b[2])
    elif abc_b[0]==abc_b[2]:
      print(abc_b[1])
    else:
      print(abc_b[0])
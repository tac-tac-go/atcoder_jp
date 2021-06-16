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
        input = """1"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2"""
        output = """31"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7"""
        output = """97656"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  result=1
  person=1
  for i in range(1,n+1):
    result=result*5
    person+=result
  print(person)
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
        input = """1"""
        output = """1005"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  t = int(input())
  num1 = t
  num2 = 40-t+1
  result = [num1,num2]
  add = 40
  for i in range(4):
    result.append(num1+add)
    result.append(num2+add)
    add+=40
  print(sum(result))


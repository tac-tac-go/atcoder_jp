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
        input = """11"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100"""
        output = """25"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10000"""
        output = """1229"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  count=0
  for i in range(2,n):
    for j in range(2,i):
      if i % j == 0:
        break
    else:
      count+=1
  print(count)
    

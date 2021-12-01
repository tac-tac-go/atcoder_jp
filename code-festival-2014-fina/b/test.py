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
        input = """13458"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """2525"""
        output = """-6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  s = list(map(int,list(input())))
  result=0
  for i,v in enumerate(s):
    if (i+1)%2==1:
      result+=v
    else:
      result-=v
  print(result)
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
        input = """229 390"""
        output = """Hard"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """123456789 9876543210"""
        output = """Easy"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  a,b = input().split()
  a = a.zfill(max(len(a),len(b)))
  b = b.zfill(max(len(a),len(b)))
  result="Easy"
  for ai,bi in zip(a,b):
    if int(ai)+int(bi)>=10:
      result="Hard"
      break
    else:
      continue
  print(result)
  

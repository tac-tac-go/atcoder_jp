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
        input = """mari
to
zzo
1321"""
        output = """marizzotomari"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """abra
cad
abra
123"""
        output = """abracadabra"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """a
b
c
1"""
        output = """a"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  s = [input(),input(),input()]
  tn = map(int,list(input()))
  result=""
  for t in tn:
    result+=s[t-1]
  print(result)
    


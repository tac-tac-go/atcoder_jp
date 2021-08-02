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
        input = """7777"""
        output = """Weak"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0112"""
        output = """Strong"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9012"""
        output = """Weak"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  X= list(map(int,list(input())))
  if(len(set(X))==1):
    print("Weak")
  else:
    X1 = ((X[0]+1)%10) == X[1]
    X2 = ((X[1]+1)%10) == X[2]
    X3 = ((X[2]+1)%10) == X[3]
    if(X1 and X2 and X3):
      print("Weak")
    else:
      print("Strong")
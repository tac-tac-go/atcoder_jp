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
        input = """3 0 10"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 2 10"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  a,b,c = map(int,input().split())
  result=0
  index=0
  while result<c:
    result+=a
    if (index+1)%7==0:result+=b
    index+=1
  print(index)
  
  


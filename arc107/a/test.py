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
        input = """1 2 3"""
        output = """18"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000000000 987654321 123456789"""
        output = """951633476"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  a,b,c = map(int,input().split())
  count=0
  for i in range(1,a+1):
    for j in range(1,b+1):
      for k in range(1,c+1):
        count+=(i*j*k)
  print(count%998244353)

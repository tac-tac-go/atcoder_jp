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
        input = """1 0"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 5"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10"""
        output = """213"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """30 100"""
        output = """2471"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  s,t = map(int,input().split())
  result=[]
  for i1 in range(101):
    for i2 in range(101):
      for i3 in range(101):
        if i1+i2+i3<=s:
          result.append([i1,i2,i3])
  count=0
  for a,b,c in result:
    if a*b*c<=t:count+=1
  print(count)
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
        input = """1 60 20 100
72 28"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 70 70 150
72 77
70 90
65 88
75 75
97 84"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """15 80 60 150
20 24
33 17
29 36
40 18
15 27
10 41
53 77
42 15
12 17
32 10
19 28
37 27
91 2
13 25
40 40"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n,x,y,z = map(int,input().split())
  ab = [map(int,input().split()) for i in range(n)]
  count=0
  for a,b in ab:
    if (a>=x and b>=y) and (a+b>=z):count+=1
  print(count)

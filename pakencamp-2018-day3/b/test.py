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
        input = """3
700
700
700"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
2018
1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
10000"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """20
188
186
234
175
172
157
244
108
81
297
331
323
185
162
216
143
141
225
200
177"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  year=0;count=0
  for i in range(n):
    year+=int(input()) 
    if year <=2018:count+=1
  print(count)


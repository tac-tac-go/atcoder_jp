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
5
10
20"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
8
15
30"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
3
5
50"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  a = int(input())
  b = int(input())
  c = int(input())
  s = int(input())
  q1 = [a, a+1]
  q2 = [b, b+1]
  q3 = [c, c+1]
  flag = False
  for i1 in q1:
    for i2 in q2:
      for i3 in q3:
        if i1+i2+i3 == s:
            flag = True
            break
  print("Yes") if flag else print("No")



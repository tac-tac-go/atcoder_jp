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
        input = """3 2
Joi"""
        output = """JOI"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1
O"""
        output = """o"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 3
JoIOji"""
        output = """JoioJI"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def judge(char):
  if char.islower():
      return char.upper()
  else:
    return char.lower()

def resolve():
  n,k = map(int,input().split())
  t = input()
  if n==1:
    result = judge(t)
    print(result)
  else:
    result=t[:k-1]
    for i in range(k-1,n):
      char = t[i]
      judge_t = judge(char)
      result += judge_t
    print(result)
    

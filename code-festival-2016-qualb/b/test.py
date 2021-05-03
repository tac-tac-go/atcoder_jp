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
        input = """10 2 3
abccabaabb"""
        output = """Yes
Yes
No
No
Yes
Yes
Yes
No
No
No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """12 5 2
cabbabaacaba"""
        output = """No
Yes
Yes
Yes
Yes
No
Yes
Yes
No
Yes
No
No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 2 2
ccccc"""
        output = """No
No
No
No
No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n,a,b = map(int,input().split())
  s = list(input())
  pass_c =0
  pass_f =0
  for i,s_v in enumerate(s):
    if s_v =="a":
      if pass_c<a+b:
        print("Yes")
        pass_c+=1
      else:
        print("No")
    elif s_v=="b":
      if pass_c<a+b and (pass_f<b):
        print("Yes")
        pass_c+=1
        pass_f+=1
      else:
        print("No")
    else:
      print("No")


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
        input = """abc
acb"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """aabb
bbaa"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """abcde
abcde"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  s = input()
  t = input()
  flag=False
  if s==t:
      print("Yes")
  else:
    for i in range(0,len(s)-1):
        if s[:i]+s[i:i+2][::-1]+s[i+2:]==t:
            flag=True
            break
    print("Yes") if flag else print("No")

  

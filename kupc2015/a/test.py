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

    def test_入力例(self):
        input = """3
higashikyoto
kupconsitetokyotokyoto
goodluckandhavefun"""
        output = """1
2
0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  t = int(input())
  s = [input() for i in range(t)]
  for si in s:
      si_l = len(si)
      i = 0
      count=0
      while i<si_l:
          if si[i:i+5] == "kyoto" or si[i:i+5]=="tokyo":
            i+=5
            count+=1
          else:
            i+=1
      print(count)
      

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

    def test_入力例1(self):
        input = """4 10
11 9 15 13"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5 10000
763618767 814402216 467921615 163029185 204341760"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n, k = map(int, input().split())
  an = list(map(int, input().split()))
  max_val = -1
  flag = False
  for ai in an:
    if k >= ai:
      if max_val < ai:
        max_val = ai
        flag = True
  print(an.index(max_val)+1) if flag else print(-1)

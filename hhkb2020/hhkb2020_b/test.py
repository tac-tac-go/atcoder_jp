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
        input = """2 3
..#
#.."""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2
.#
#."""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  import numpy as np
  h,w = map(int,input().split())
  s = np.array([list(input()) for i in range(h)])
  count=0
  for i in range(h):
    for j in range(0,w-1):
      if "".join(s[i,j:j+2])=="..":count+=1
  
  for i in range(w):
    for j in range(0,h-1):
      if "".join(s[j:j+2,i])=="..":
        count+=1
  print(count)

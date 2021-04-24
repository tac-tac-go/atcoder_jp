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
        input = """4 4
##.#
....
##.#
.#.#"""
        output = """###
###
.##"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
#..
.#.
..#"""
        output = """#..
.#.
..#"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 5
.....
.....
..#..
....."""
        output = """#"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """7 6
......
....#.
.#....
..#...
..#...
......
.#..#."""
        output = """..#
#..
.#.
.#.
#.#"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  import numpy as np
  h,w = map(int,input().split())
  a = np.array([list(input()) for i in range(h)])
  result=[]
  for i in range(h):
    if (a[i,:]=="#").any():
      result.append(list(a[i,:]))
  b=np.array(result)

  result2=[]
  for j in range(w):
    if (a[:,j]=="#").any():
      result2.append(list(b[:,j]))
  c = np.array(result2).T
  for k in range(len(c)):
    print("".join(c[k,:]))
      


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
        input = """3 3
2 1 4
3 1 3
6 4 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 4
4 3 2 1
5 6 7 8"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  h,w = map(int,input().split())
  import numpy as np
  A = np.array([list(map(int,input().split())) for _ in range(h)])
  import itertools
  bool = "Yes"
  for i in list(itertools.combinations(range(h), 2)):
    for j in list(itertools.combinations(range(w), 2)):      
      if A[i[0], j[0]] + A[i[1], j[1]] > A[i[1], j[0]] + A[i[0], j[1]]:        
        bool = "No"
        break
    else:
        continue
    break
  print(bool)

  
  

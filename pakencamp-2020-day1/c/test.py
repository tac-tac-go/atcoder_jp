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
        input = """2
2
kaage penguinman
2
penguinman rho"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3
1
penguinman
1
kaage
1
rho"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """3
3
a b c
2
a ba
3
a ba abc"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  name = []
  name3 = []
  for _ in range(n):
    k = input()
    v = input().split()
    name.extend(v)
    name3.append(v)
  name2 = list(set(name))
  from collections import defaultdict
  result = defaultdict(list)
  for i in name2:
      result[i]=0
  result = dict(result)
  for i in name3:
      for j in i:
          result[j]+=1
  print(len(list(filter(lambda x: x == n, list(result.values())))))
  
    

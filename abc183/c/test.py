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
        input = """4 330
0 1 10 100
1 0 20 200
10 20 0 300
100 200 300 0"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 5
0 1 1 1 1
1 0 1 1 1
1 1 0 1 1
1 1 1 0 1
1 1 1 1 0"""
        output = """24"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()


def resolve():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    from itertools import permutations
    path = list(range(2, n+1))
    result=0
    for v in permutations(path, len(path)):
      path_i = [1] + list(v) + [1]
      count = 0
      for i in range(len(path_i)-1):
        count += t[path_i[i]-1][path_i[i+1]-1]
      if count==k:result+=1
    print(result)

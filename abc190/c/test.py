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
1 2
1 3
2 4
3 4
3
1 2
1 3
2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 4
1 2
1 3
2 4
3 4
4
3 4
1 2
2 4
2 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 12
2 3
4 6
1 2
4 5
2 6
1 5
4 5
1 3
1 2
2 6
2 3
2 5
5
3 5
1 4
2 6
4 6
5 6"""
        output = """9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  N, M = map(int, input().split())
  zyouken = []
  for i in range(M):
      a, b = map(int, input().split())
      zyouken.append([a, b])
  K = int(input())
  okikata = []
  for i in range(K):
      c, d = map(int, input().split())
      okikata.append([c, d])
  maximum = -9999
  for i in range(2**K):
      f = "{{:0{}b}}".format(K)
      judge = f.format(i)
      ball = [0 for i in range(N)]
      for j in range(K):
          if judge[j] == "1":
              ball[okikata[j][0]-1] += 1
          else:
              ball[okikata[j][1]-1] += 1
      now = 0
      for j in range(M):
          if ball[zyouken[j][0]-1] >= 1 and ball[zyouken[j][1]-1] >= 1:
              now += 1
      if now > maximum:
          maximum = now
  print(maximum)



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
        input = """4
0 1
1 3
1 1
-1 -1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20
224 433
987654321 987654321
2 0
6 4
314159265 358979323
0 0
-123456789 123456789
-1000000000 1000000000
124 233
9 -6
-4 0
9 5
-7 3
333333333 -333333333
-9 -1
7 -10
-1 5
324 633
1000000000 -1000000000
20 0"""
        output = """1124"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  xy = [list(map(int,input().split())) for i in range(n)]
  count=0
  for i1 in range(1,n-1):
    for i2 in range(i1+1,n):
        for i3 in range(i2+1,n+1):
            point = [xy[i1-1], xy[i2-1], xy[i3-1]]
            point.sort()
            point1 = point[0]
            point2 = point[1]
            point3 = point[2]
            dx2 = point3[0]-point1[0]
            dx1 = point2[0]-point1[0]
            dy1 = point2[1]-point1[1]
            dy2 = point3[1]-point1[1]
            if dx2*dy1 != dx1*dy2:count+=1
  print(count)


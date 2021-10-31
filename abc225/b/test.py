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
        input = """5
1 4
2 4
3 4
4 5"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
2 4
1 4
2 3"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
9 10
3 10
4 10
8 10
1 10
2 10
7 10
6 10
5 10"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  count = [0]*n
  for i in range(n-1):
    a,b = map(int,input().split())
    count[a-1]+=1
    count[b-1]+=1
  print("Yes") if max(count)==n-1 else print("No")

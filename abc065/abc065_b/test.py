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
        input = """3
3
1
2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
3
4
1
2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
3
3
4
2
4"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  a = [int(input()) for i in range(n)]
  count=1
  flag=False
  now =a[0]
  for i in range(n):
    if now ==2:
      flag=True
      break
    count+=1
    now = a[now-1]
  print(count) if flag else print(-1)
   
  
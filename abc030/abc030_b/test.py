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
        input = """15 0"""
        output = """90"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 17"""
        output = """3.5"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """0 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """6 0"""
        output = """180"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """23 59"""
        output = """5.5000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n,m = map(int,input().split())
  n = n%12
  n_r = (n%12)*30+(m/60)*30
  m_r = (m/60)*360
  a = max(n_r,m_r)-min(n_r,m_r)
  b = (360-max(n_r,m_r))+min(n_r,m_r)
  print(min(a,b))

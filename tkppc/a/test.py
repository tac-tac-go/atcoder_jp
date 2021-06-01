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
10 3
5 11"""
        output = """13
16"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3
5 16
59 14
3 17"""
        output = """21
73
20"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """10
67 41
0 34
24 69
58 78
64 62
45 5
27 81
91 61
42 95
36 27"""
        output = """108
34
93
136
126
50
108
152
137
63"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  ab = [print(sum(map(int,input().split()))) for _ in range(n)]
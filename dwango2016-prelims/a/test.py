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
        input = """42"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """20160123"""
        output = """806404"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
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
        input = """42"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """20160123"""
        output = """806404"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()


def make_divisors(N):
    divisors = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            divisors.append(i)
            if i != N // i:
                divisors.append(N//i)
    return divisors

def resolve():
  n = int(input())
  print(n//25)






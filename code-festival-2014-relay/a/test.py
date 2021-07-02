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
        input = """3"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()


def prime_check(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def prime_check(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def resolve():
  n = int(input())
  result=[]
  for x in range(2, n+1):
    if prime_check(x):
        result.append(x)
  print(len(list(filter(lambda x:x%2==0,result))))

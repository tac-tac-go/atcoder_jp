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
        input = """1 + 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5 - 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """10 * 20"""
        output = """200"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """10 / 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """100 / 0"""
        output = """error"""
        self.assertIO(input, output)

    def test_入力例6(self):
        input = """25 ? 31"""
        output = """error"""
        self.assertIO(input, output)

    def test_入力例7(self):
        input = """0 + 0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  aorb = input()
  try :
    print(int(eval(aorb)))
  except:
    print("error")

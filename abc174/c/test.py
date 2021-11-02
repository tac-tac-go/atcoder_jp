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
        input = """101"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """999983"""
        output = """999982"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  K = int(input())
  count = 1
  mod = 7

  for i in range(K):
    if mod % K ==0:
      break
    count +=1
    mod = (mod * 10 + 7) % K
  
  if mod%K ==0:
    print(count)
  else:
    print(-1)
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
        input = """123"""
        output = """63"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1010"""
        output = """100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """998244353"""
        output = """939337176"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = list(input())
  d = len(n)
  ans = 0
  
  def pick(bit):
    use = []
    for i in range(d):
      if (bit >> i) %2 ==1:
        use.append(n[i])
    use.sort(reverse=True)
    return int(''.join(use))
  
  for bit in range(1,(1<<d)-1):
    other = ((1 << d) -1) ^bit #全てのbitが立っている状態の反対
    ans = max(ans,pick(bit) * pick(other))
  print(ans)



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
        input = """2
FLIP
2
2 0 0
1 1 4"""
        output = """LPFI"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
FLIP
6
1 1 3
2 0 0
1 1 2
1 2 3
2 0 0
1 1 4"""
        output = """ILPF"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
    n = int(input())
    s = list(input())
    q = int(input())

    result = s
    flip_flag = False

    for i in range(q):
        t,a,b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            if flip_flag:
                result[a-n], result[b-n] = result[b-n], result[a-n]
            else:
                result[a], result[b] = result[b], result[a]
        else:
            flip_flag = not flip_flag

    if flip_flag:
        result = result[n:] + result[:n]
    print(''.join(result))


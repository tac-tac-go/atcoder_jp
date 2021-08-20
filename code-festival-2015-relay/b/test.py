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
        input = """oxxxxxxxxx
xoxxxxxxxx
xxoxxxxxxx
xxxoxxxxxx
xxxxoxxxxx
xxxxxoxxxx
xxxxxxoxxx
xxxxxxxoxx
xxxxxxxxox
xxxxxxxxxo"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """xxxxxxxxxx
xxxxxxxxxx
xxxxxxxxxx
xxxxxxxxxx
xxxxxxxxxx
xxxxxxxxxx
xxxxxxxxxx
xxxxxxxxxx
xxxxxxxxxx
oooooooooo"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """oxxxxxxxxx
ooxxxxxxxx
ooxoxxxxxx
oooxoxxxxx
oxxxxooxxx
ooxoxxoxxx
oooooxxxxx
ooooxxoxxx
ooooxoxxox
oooooooxxo"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()


def resolve():
    p = [list(input()) for i in range(10)]
    array = [0]*10
    for p_r in p:
        for i, p_c in enumerate(p_r):
            if p_c == "o":
                array[i] += 1
    print("Yes") if min(array)>=1 else print("No")
    

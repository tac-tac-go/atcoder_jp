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
        input = """##
.#"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """.#
#."""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
    s1 = list(input())
    s2 = list(input())
    if (s1[0] == "." and s1[1] == "#" and s2[0] == "#" and s2[1] == ".") or (s1[0] == "#" and s1[1] == "." and s2[0] == "." and s2[1] == "#"):print("No")
    else:print("Yes")

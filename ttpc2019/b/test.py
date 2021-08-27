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
        input = """1
tokyoinstituteoftechnology"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8
okyoech
tokyotech
titech
tokyotokyotechtech
tokyotecg
tttoookkkyyyooottteeeccchhh
tokyokogyodaigaku
tokyouniversityofagricultureandtechnology"""
        output = """Yes
Yes
No
Yes
No
No
No
Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  import re
  n = int(input())
  pattern = ".*okyo.*ech.*"
  for i in range(n):
    s = input()
    flag = re.match(pattern,s)
    if flag!=None:
      print("Yes")
    else:
      print("No")


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
        input = """3
tanaka taro
sato hanako
tanaka taro"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
saito ichiro
saito jiro
saito saburo"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
sypdgidop bkseq
bajsqz hh
ozjekw mcybmtt
qfeysvw dbo"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  a = [input().split() for i in range(n)]
  flag=False
  for i in range(n):
    for j in range(i+1,n):
      if a[i][0]==a[j][0] and a[i][1]==a[j][1]:
        flag=True
        break
    if flag:break
  print("Yes") if flag else print("No")
    

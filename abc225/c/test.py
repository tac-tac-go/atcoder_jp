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
        input = """2 3
1 2 3
8 9 10"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 1
1
2"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 4
1346 1347 1348 1349
1353 1354 1355 1356
1360 1361 1362 1363
1367 1368 1369 1370
1374 1375 1376 1377
1381 1382 1383 1384
1388 1389 1390 1391
1395 1396 1397 1398
1402 1403 1404 1405
1409 1410 1411 1412"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  yes,no='Yes','No'
  N,M=map(int,input().split())
  B=[list(map(int,input().split())) for _ in range(N)]
  f=B[0][0]
  if (f-1)%7+M>7:
      print(no)
      exit()
  for i in range(N):
      for j in range(M):
          if B[i][j]!=f+i*7+j:
              print(no)
              exit()
  print(yes)
  
      

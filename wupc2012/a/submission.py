ma, da = map(int, input().split())
mb, db = map(int, input().split())
month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if ma == mb:
  print(db-da)
else:
  count = 0
  print(sum([month[i-1] for i in range(ma, mb, 1)])-da+db)

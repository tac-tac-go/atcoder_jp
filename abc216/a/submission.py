x, y = map(int, input().split("."))
print("{}{}".format(x, "-")) if 0 <= y and 2 >= y else print(
    x) if 3 <= y and 6 >= y else print("{}{}".format(x, "+"))

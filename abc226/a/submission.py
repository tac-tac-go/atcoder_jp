from decimal import Decimal, ROUND_HALF_UP
x = float(input())
a = Decimal(str(x))
b = a.quantize(Decimal('0'), rounding=ROUND_HALF_UP)
print(b)

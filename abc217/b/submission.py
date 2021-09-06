s1 = input()
s2 = input()
s3 = input()
print(list(set(["ABC", "ARC", "AGC", "AHC"])-set([s1, s2, s3]))[0])

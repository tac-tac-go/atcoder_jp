S = input()
result = []
for i in range(0,len(S)-2,1):
  result.append(abs(753-int(S[i:i+3])))
print(min(result))    
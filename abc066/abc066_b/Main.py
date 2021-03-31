import math
S = input()
for i in range(len(S)-1,0,-1):
  S = S[:i]
  if S[:math.ceil(len(S)/2)]==S[math.ceil(len(S)/2):]:
    print(len(S))
    break
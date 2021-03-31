N = input()
S = input()
print(len([i for i in range(0,len(S)-2) if S[i:i+3]=="ABC"]))
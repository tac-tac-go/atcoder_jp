S = input()
N = int(input())
st = set()
if N<=len(S):
    for i in range(len(S)-N+1):
        st.add(S[i:i+N])
print(len(st))
N = int(input())
D = [list(map(int,input().split())) for _ in range(N)]
out_text = "No"
for index in range(N-2):
    if D[index][0]==D[index][1] and D[index+1][0]==D[index+1][1] and D[index+2][0]==D[index+2][1]:
      out_text="Yes"
      break
print(out_text)
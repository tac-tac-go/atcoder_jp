word = sorted(list(input()))
N = int(input())
word_list = [i+j for i in word for j in word]
print(word_list[N-1])
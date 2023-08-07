word = 'abcba'
N = len(word)

for i in range(N//2):
    if word[i] != word[N-1-i]:
        return
    else:
        pass


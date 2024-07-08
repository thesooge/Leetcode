word = "abcdefd"
ch = "d"
new_word = ""
for i in range(len(word)):
    if word[i] == ch:
        new_word = word[:word.index(word[i])+1]
        word = word.removeprefix(word[:word.index(word[i])+1])
        break

new_word = new_word[::-1]

print(new_word+word)    
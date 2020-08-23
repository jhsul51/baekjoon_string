alphabet = [-1]*26
word = input()
for c in word:
    if alphabet[ord(c)-97] == -1:
        alphabet[ord(c)-97] = word.index(c)
for al in alphabet:
    print(al, end=" ")
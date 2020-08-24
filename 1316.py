n = int(input())
count =0
def group(word):
    temp = word[0]
    buf = list()
    for i in range(1,len(word)):
        if word[i] in buf:
            return False
        if temp != word[i]:
            buf.append(temp)
            temp = word[i]
        else:
            pass
    return True

            
for i in range(n):
    word = input()
    if group(word) == True:
        count += 1
print(count)

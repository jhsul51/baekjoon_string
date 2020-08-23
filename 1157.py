n = input().upper()
charlist = list(set(n))
countlist = list()
for c in charlist:
    countlist.append(n.count(c)) 
if countlist.count(max(countlist)) != 1:
    print("?")
else:
    print(charlist[countlist.index(max(countlist))])

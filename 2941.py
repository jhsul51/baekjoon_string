croatia = ['c=', 'c-', 'dz=','d-','lj','nj','s=','z=']
word = input()
bufftyp = ''
count = 0
for c in word:
    bufftyp += c
    if len(bufftyp) < 2 or bufftyp == 'dz':
        pass
    elif bufftyp in croatia:
        count += 1
        bufftyp = ''
    else:
        count += len(bufftyp)-1
        bufftyp = list(bufftyp).pop()

count += len(bufftyp)
bufftyp = ''
print(count)
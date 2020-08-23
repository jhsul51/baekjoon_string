import sys
n = list(sys.stdin.readline().strip().split(" "))
while n.count('')>0:
    n.remove('')
while n.count('\n')>0:
    n.remove('\n')
print(len(n))
import sys
def frog(n):
    n = int(n)
    m = n//100 + ((n//10)%10)*10 + (n%10)*100
    return m

print(max(list(map(frog, sys.stdin.readline().split()))))
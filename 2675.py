case = int(input())
for i in range(case):
    n, st = input().split()
    n = int(n)
    code = ""
    for c in st:
        code += c*n
    print(code)
# BOJ 1874 스택 수열
from sys import stdin

stack, result = [], []
m, isNo = 0, False
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    for i in range(m+1, n+1):
        stack.append(i)
        result.append('+')
    p = stack.pop()
    if p != n:
        isNo = True
        print("NO")
        break
    m = max(p, m)
    result.append('-')
if not isNo:
    print('\n'.join(result))

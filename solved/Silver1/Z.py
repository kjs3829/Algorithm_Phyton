# BOJ 1074 Z
from sys import stdin

N, r, c = map(int, stdin.readline().split())
result = 0
for n in range(N, 0, -1):
    u = r // 2**(n-1)
    d = c // 2**(n-1)
    if u==0 and d==1:
        result += 2 ** (2*n-2) * 1
    elif u==1 and d==0:
        result += 2 ** (2*n-2) * 2
    elif u==1 and d==1:
        result += 2**(2*n-2) * 3
    r -= 2**(n-1) * u
    c -= 2**(n-1) * d
print(result)


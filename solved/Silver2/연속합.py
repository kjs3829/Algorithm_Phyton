# BOJ 1912 연속합

from sys import stdin
n = int(stdin.readline())
p = list(map(int, stdin.readline().split()))
result, s = p[0], 0
for i in range(n):
    s += p[i]
    if s < p[i]:
        s = p[i]
    if result < s:
        result = s
print(result)


# Baekjoon 1158 요세푸스 문제

import sys

N, K = map(int, sys.stdin.readline().split())
p = list(range(1, N+1))
r = []
i = K-1
while 1:
    r.append(p.pop(i))
    if not p:
        break
    i = (i+K-1) % len(p)
print('<'+','.join(map(str, r)) + '>')

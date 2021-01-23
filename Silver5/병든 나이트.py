# Baekjoon 1783 병든 나이트

import sys

N, M = map(int, sys.stdin.readline().split())

if N == 1 or M == 1 :
    cnt = 1
elif M >= 7:
    if N >= 3:
        cnt = (M-6) + 4
    else:
        cnt = 4
elif M in (4, 5, 6):
    if N >= 3:
        cnt = 4
    else:
        cnt = (M+1) // 2

elif M in (2, 3):
    if N >= 3:
        cnt = M
    else:
        cnt = (M+1) // 2

print(cnt)

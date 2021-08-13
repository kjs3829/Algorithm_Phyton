# BOJ 1049 기타줄
# 수학

import sys

N, M = map(int, sys.stdin.readline().split())
six, one = map(int, sys.stdin.readline().split())
for _ in range(M-1):
    a, b = map(int, sys.stdin.readline().split())
    six = a if a < six else six
    one = b if b < one else one

cost = 0
if one * 6 < six:
    cost = one * N
else:
    cost = N // 6 * six
    if N % 6 * one > six:
        cost += six
    else:
        cost += N % 6 * one
print(cost)

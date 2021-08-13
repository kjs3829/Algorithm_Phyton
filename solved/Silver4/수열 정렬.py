# Baekjoon 1015 수열 정렬

import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = []
for idx in range(N):
    B.append([A[idx], idx])

B.sort(reverse=False, key=lambda x: x[0])
P = [0]*N
for idx in range(len(B)):
    P[B[idx][1]] = idx
for c in P:
    print(c, end=' ')



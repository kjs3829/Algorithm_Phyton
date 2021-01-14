# Baekjoon 1495 기타리스트

import sys
N, S, M = map(int, sys.stdin.readline().split())
V = list(map(int, sys.stdin.readline().split()))
V.insert(0, 0)
dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][S] = 1
for i in range(1, N+1):
    for x in range(M+1):
        if dp[i-1][x] == 0:
            continue
        if x + V[i] <= M:
            dp[i][x + V[i]] = 1
        if x - V[i] >= 0:
            dp[i][x - V[i]] = 1

result = -1
for idx in range(M+1):
    if dp[N][idx]:
        result = idx
print(result)


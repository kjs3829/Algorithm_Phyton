# BOJ 11048 이동하기
# DP
from sys import stdin

N, M = map(int, stdin.readline().split())
dp = [[0]*(M+1)]
for i in range(N):
    candy = [0] + list(map(int, stdin.readline().split()))
    dp.append(candy)
for r in range(1, N+1):
    for c in range(1, M+1):
        dp[r][c] += max(dp[r-1][c], dp[r][c-1])
print(dp[N][M])

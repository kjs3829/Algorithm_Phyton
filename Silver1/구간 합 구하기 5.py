# BOJ 11660 구간 합 구하기 5
# DP
from sys import stdin

N, M = map(int, stdin.readline().split())
dp = [[0]*(N+1) for _ in range(N+1)]
for r in range(1, N+1):
    tmp = list(map(int, stdin.readline().split()))
    for i in range(1, N+1):
        dp[r][i] = dp[r-1][i] + dp[r][i-1] + tmp[i-1] - dp[r-1][i-1]
for _ in range(M):
    x1,y1,x2,y2 = map(int, stdin.readline().split())
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])

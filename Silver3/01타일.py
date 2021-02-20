# BOJ 1904 01타일
# DP
from sys import stdin

N = int(stdin.readline())
if N == 1:
    print(1)
else:
    dp = [0] * N
    dp[0], dp[1] = 1, 2
    for i in range(2, N):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 15746
    print(dp[N - 1])

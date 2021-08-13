# Baekjoon 1463 1로 만들기

import sys

N = int(sys.stdin.readline())
dp = [0]*1000001
dp[1] = 0
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i // 3] + 1
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i // 2] + 1
print(dp[N])


# Baekjoon 1309 동물원

import sys

N = int(sys.stdin.readline())

dp = [[0]*3 for _ in range(N+1)]
dp[1][0], dp[1][1], dp[1][2] = 1, 1, 1

for i in range(2, N+1):
    dp[i][0] = dp[i-1][1] + dp[i-1][2] % 9901
    dp[i][1] = dp[i-1][0] + dp[i-1][2] % 9901
    dp[i][2] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2] % 9901

print((dp[N][0]+dp[N][1]+dp[N][2]) % 9901)


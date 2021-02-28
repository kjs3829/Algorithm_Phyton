# BOJ 15988 1,2,3 더하기 3
# DP
import sys
input = sys.stdin.readline

dp = [0 for i in range(1000001)]
dp[0], dp[1], dp[2] = 1, 1, 2
for i in range(3, 1000001):
    dp[i] = dp[i - 1] % 1000000009 + dp[i - 2] % 1000000009 + dp[i - 3] % 1000000009

for i in range(int(input())):
    n = int(input())
    print(dp[n] % 1000000009)

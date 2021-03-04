# BOJ 1535 안녕
# DP, 0/1 knapsack
import sys
input = sys.stdin.readline

n = int(input())
h = [0] + list(map(int, input().split()))
e = [0] + list(map(int, input().split()))
dp = [[0]*101 for _ in range(21)]
for i in range(1, n+1):
    for health in range(1, 101):
        if h[i] < health:
            dp[i][health] = max(dp[i-1][health], dp[i-1][health-h[i]]+e[i])
        else:
            dp[i][health] = dp[i-1][health]
print(dp[n][100])

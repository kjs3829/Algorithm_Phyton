# Baekjoon 1010 다리 놓기

T = int(input())
for x in range(T):
    N, M = map(int, input().split())
    dp = [[0]*31 for _ in range(31)]

    for x in range(M):
        dp[0][x] = x+1

    for n in range(1, N):
        for m in range(M):
            if n == m:
                dp[n][m] = 1
            elif m == n + 1:
                dp[n][m] = m+1
            else:
                dp[n][m] = dp[n - 1][m - 1] + dp[n][m - 1]
    print(dp[N-1][M-1])

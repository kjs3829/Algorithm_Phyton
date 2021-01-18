# Baekjoon 1520 내리막길

import sys
sys.setrecursionlimit(10000)
dr = [0,1,0,-1]
dc = [1,0,-1,0]


def dfs_dp(r, c):
    if r == R - 1 and c == C - 1:
        return 1
    if dp[r][c] != -1:
        return dp[r][c]
    dp[r][c] = 0
    for n in range(4):
        nr = r + dr[n]
        nc = c + dc[n]
        if -1 < nr < R and -1 < nc < C:
            if mat[r][c] > mat[nr][nc]:
                dp[r][c] += dfs_dp(nr, nc)
    return dp[r][c]


input = sys.stdin.readline
R, C = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(R)]
dp = [[-1]*C for _ in range(R)]
print(dfs_dp(0, 0))

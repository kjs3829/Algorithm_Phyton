# BOJ 1012 유기농 배추
# 그래프 이론
from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10**6)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    if 0 <= x < W and 0 <= y < H and mat[y][x] == 1:
        mat[y][x] = 0
        for i in range(4):
            dfs(x+dx[i], y+dy[i])


for _ in range(int(stdin.readline())):
    W, H, K = map(int, stdin.readline().split())
    mat = [[0]*W for _ in range(H)]

    for _ in range(K):
        a, b = map(int, stdin.readline().split())
        mat[b][a] = 1

    cnt = 0
    for r in range(H):
        for c in range(W):
            if mat[r][c] == 1:
                cnt += 1
                dfs(c, r)
    print(cnt)


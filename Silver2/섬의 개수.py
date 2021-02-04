# BOJ 4963 섬의 개수
# 그래프 이론, DFS
from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10 ** 6)
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]


def dfs(x, y):
    if 0 <= x < w and 0 <= y < h and mat[y][x] == 1:
        mat[y][x] = 0
        for i in range(8):
            dfs(x + dx[i], y + dy[i])
        return True
    return False


while True:
    w, h = map(int, stdin.readline().split())
    if w == 0 and h == 0:
        break
    mat = []
    for _ in range(h):
        mat.append(list(map(int, stdin.readline().split())))

    cnt = 0

    for x in range(w):
        for y in range(h):
            if dfs(x, y):
                cnt += 1
    print(cnt)

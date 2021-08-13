# BOJ 2589 보물섬
# 너비 우선 탐색
# Python3로 제출하면 시간초과가 떠서 PyPy3로 제출함
import sys
from collections import deque
input = sys.stdin.readline
dx=[1,0,-1,0]
dy=[0,1,0,-1]


def bfs(w, h):
    visit = [[0] * width for _ in range(height)]
    queue = deque([[w, h]])
    visit[h][w] = 1
    num = 0
    while queue:
        x, y = queue.popleft()
        for idx in range(4):
            ny, nx = y + dy[idx], x + dx[idx]
            if 0 <= ny < height and 0 <= nx < width:
                if mat[ny][nx] == 'L' and visit[ny][nx] == 0:
                    queue.append([nx, ny])
                    visit[ny][nx] = visit[y][x] + 1
                    num = max(num, visit[ny][nx])
    return num - 1


height, width = map(int, input().split())
mat = [list(map(str, input())) for _ in range(height)]
result = 0
for h in range(height):
    for w in range(width):
        if mat[h][w] == 'L':
            result = max(result, bfs(w, h))
print(result)


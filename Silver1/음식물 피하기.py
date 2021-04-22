# BOJ 1743 음식물 피하기
# 그래프 탐색
import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]


def bfs(r,c):
    q = deque()
    q.append([r,c])
    mat[r][c] += 1
    cnt = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= ny < N and 0 <= nx < M and mat[ny][nx] == 1:
                q.append([ny, nx])
                mat[ny][nx] += 1
                cnt += 1
    return cnt


def dfs(r,c):
    stack = [[r,c]]
    mat[r][c] += 1
    cnt = 0
    while stack:
        p = stack.pop()
        cnt += 1
        for i in range(4):
            x, y = p[1] + dx[i], p[0] + dy[i]
            if 0 <= x < M and 0 <= y < N and mat[y][x] == 1:
                stack.append([y,x])
                mat[y][x] += 1

    return cnt


N, M, K = map(int, input().split())    # 1 <= N <= 100, 1 <= M <= 100, 1 <= K <= 10000
mat = [[0]*M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    mat[r-1][c-1] = 1
answer = 0

for r in range(N):
    for c in range(M):
        if mat[r][c] == 1:
            cnt = bfs(r,c)
            if answer < cnt:
                answer = cnt
print(answer)

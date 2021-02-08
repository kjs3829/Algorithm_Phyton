# BOJ 7569 토마토
# 3차원 BFS
from sys import stdin
from collections import deque
dx=[0,1,0,-1,0,0]
dy=[-1,0,1,0,0,0]
dz=[0,0,0,0,-1,1]


def bfs():
    while q:
        c = q.popleft()
        for i in range(6):
            z = c[0] + dz[i]
            y = c[1] + dy[i]
            x = c[2] + dx[i]
            if 0<=z<H and 0<=y<N and 0<=x<M and mat[z][y][x] == 0:
                q.append([z,y,x])
                mat[z][y][x] = mat[c[0]][c[1]][c[2]] + 1


M, N, H = map(int, stdin.readline().split())
mat = [[0]*N for _ in range(H)]
for h in range(H):
    for n in range(N):
        mat[h][n] = list(map(int, stdin.readline().split()))
q = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if mat[h][n][m] == 1:
                q.append([h,n,m])
bfs()
max_sum = 0
isAble = False
for h in range(H):
    for n in range(N):
        for m in range(M):
            if mat[h][n][m] == 0:
                isAble = True
                break
            max_sum = max(max_sum, mat[h][n][m])
if isAble:
    print(-1)
else:
    print(max_sum - 1)

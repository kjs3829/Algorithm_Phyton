# BOJ 10157 자리배정
from sys import stdin

dx = [1,0,-1,0]
dy = [0,1,0,-1]


def move(dirc, start, k):
    global r, c
    cnt = 2
    start_x, start_y = start
    mat[start_x][start_y] = 1
    stack = [(start_x, start_y)]
    cur_x = cur_y = 0
    while True:
        while stack:
            cur_x, cur_y = stack.pop()
            nx = cur_x + dx[dirc]
            ny = cur_y + dy[dirc]

            if nx >= r or nx < 0 or ny >= c or ny < 0:
                continue
            if mat[nx][ny] != 0:
                continue
            mat[nx][ny] = cnt
            if cnt == k:
                return nx + 1, ny + 1
            stack.append((nx, ny))
            cnt += 1

        stack.append((cur_x,cur_y))

        if dirc == 0:
            dirc = 1
        elif dirc == 1:
            dirc = 2
        elif dirc == 2:
            dirc = 3
        else:
            dirc = 0


c, r = map(int, stdin.readline().split())
k = int(stdin.readline())

mat = [[0]*c for _ in range(r)]

if k > r * c:
    print(0)
else:
    if k == 1:
        print(1, 1)
    else:
        idx_x, idx_y = move(0, (0, 0), k)
        print(idx_y, idx_x)

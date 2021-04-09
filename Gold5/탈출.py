# BOJ 3055 탈출
# 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]


def bfs(start, water):
    wq = deque(water)
    aq = deque([start])
    if wq:
        water_visit[wq[0][0]][wq[0][1]] = 0
    animal_visit[aq[0][0]][aq[0][1]] = 0
    cnt = -1
    while aq:
        for i in range(len(wq)):
            wp = wq.popleft()

            for idx in range(4):
                x, y = wp[1] + dx[idx], wp[0] + dy[idx]
                if 0 <= x < C and 0 <= y < R and mat[y][x] != 'X' and mat[y][x] != 'D' and water_visit[y][x]:
                    mat[y][x] = '*'
                    wq.append([y,x])
                    water_visit[y][x] = 0

        for i in range(len(aq)):
            ap = aq.popleft()
            if ap == destiny:
                return animal_visit[ap[0]][ap[1]]

            for idx in range(4):
                x, y = ap[1] + dx[idx], ap[0] + dy[idx]
                if 0 <= x < C and 0 <= y < R and mat[y][x] != 'X' and mat[y][x] != '*' and animal_visit[y][x] == -1:
                    aq.append([y, x])
                    animal_visit[y][x] = animal_visit[ap[0]][ap[1]] + 1
        cnt += 1

    return "KAKTUS"


R, C = map(int, input().split())
mat = [['.']*C for _ in range(R)]
water_visit = [[1]*C for _ in range(R)]
animal_visit = [[-1]*C for _ in range(R)]
start, destiny = [0,0], [0,0]
water = []
for r in range(R):
    l = input().rstrip()
    for c in range(len(l)):
        if l[c] == 'S':
            start = [r,c]
        if l[c] == 'D':
            destiny = [r,c]
        if l[c] == '*':
            water.append([r,c])
        mat[r][c] = l[c]

print(bfs(start, water))

# BOJ 3190 뱀
# 자료 구조, 시뮬레이션
import sys
from collections import deque
input = sys.stdin.readline


# direction: 0=오른쪽, 1=밑, 2=왼쪽, 3=위
def turnabout(direction, c):
    result = 0
    if direction == 0:
        if c == 'L': result = 3
        else: result = 1
    elif direction == 1:
        if c == 'D': result = 2
    elif direction == 2:
        if c == 'L': result = 1
        else: result = 3
    elif direction == 3:
        if c == 'L': result = 2
    return result


snake = deque([[0, 0]])     # [x,y]
d = 0   # d: 0=오른쪽, 1=밑, 2=왼쪽, 3=위
N = int(input())
mat = [[0]*N for _ in range(N)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    mat[a-1][b-1] = 1   # 사과
L = int(input())
dc = deque([[0, ''] for _ in range(L)])
for i in range(L):
    a, b = input().split()
    dc[i][0], dc[i][1] = int(a), b

time = 0
hx, hy = 0, 0
dx, dy = [1,0,-1,0], [0,1,0,-1]
flag = False
while 1:
    if dc and time == dc[0][0]:
        d = turnabout(d, dc[0][1])
        dc.popleft()
    hx, hy = snake[0][0]+dx[d], snake[0][1]+dy[d]
    if hx >= N or hx < 0 or hy < 0 or hy >= N:      # 다음 진행해야 하는 칸이 벽인 경우 종료
        break

    # 자기 몸과 부딪히면 flag = false
    for i in snake:
        if [hx, hy] == i:
            flag = True
            break
    if flag:
        break

    if mat[hy][hx] == 0:      # 이동할 칸에 사과가 없을 경우
        snake.pop()
    else:
        mat[hy][hx] = 0
    snake.appendleft([hx, hy])
    time += 1

print(time+1)

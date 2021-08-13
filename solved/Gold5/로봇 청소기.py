# BOJ 14503 로봇 청소기
# 구현, 시뮬레이션
import sys
input = sys.stdin.readline


def left(d):
    if d==0:
        return 3
    elif d==1:
        return 0
    elif d==2:
        return 1
    else:
        return 2
N, M = map(int, input().split())
r, c, d = map(int, input().split())
mat = []
for i in range(N):
    tmp = list(map(int, input().split()))
    mat.append(tmp)
cnt = 0

dx, dy = [0,1,0,-1], [-1,0,1,0]
flag = True
while flag:
    # 현재 위치를 청소한다.
    if mat[r][c] == 0:
        mat[r][c] = -1
        cnt += 1

    for i in range(4):
        d = left(d)
        if mat[r+dy[d]][c+dx[d]] == 0:
            r, c = r+dy[d], c+dx[d]
            break
        if i == 3:
            if mat[r-dy[d]][c-dx[d]] != 1:
                r, c = r-dy[d], c-dx[d]
            else:
                flag = False

print(cnt)

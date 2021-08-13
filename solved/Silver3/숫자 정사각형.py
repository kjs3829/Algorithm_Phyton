# BOJ 1051 숫자 정사각형
# 구현, 브루트포스

import sys

N, M = map(int, sys.stdin.readline().split())
mat = [[0]*M for _ in range(N)]

for r in range(N):
    s = sys.stdin.readline().rstrip()
    for c in range(len(s)):
        mat[r][c] = s[c]
result = 1
sm = N if N < M else M
isMax = False

for max_size in range(sm, 1, -1):
    if isMax:
        break
    for r in range(N - max_size + 1):
        for c in range(M - max_size + 1):
            right = c+max_size-1
            bottom = r+max_size-1
            if mat[r][c] == mat[r][right] and mat[r][c] == mat[bottom][c] and mat[r][c] == mat[bottom][right]:
                isMax = True
                result = max_size**2
                break
print(result)

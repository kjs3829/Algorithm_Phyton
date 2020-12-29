# Baekjoon 1236 성 지키기

N, M = map(int, input().split())
mat = [input() for _ in range(N)]

x_cnt, y_cnt = 0, 0
for x in range(M):
    flag = False
    for y in range(N):
        if mat[y][x] == 'X':
            flag = True
            break
    if not flag:
        y_cnt += 1

for y in range(N):
    flag = False
    for x in range(M):
        if mat[y][x] == 'X':
            flag = True
            break
    if not flag:
        x_cnt += 1
print(x_cnt if x_cnt > y_cnt else y_cnt)




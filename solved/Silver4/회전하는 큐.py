# Baekjoon 1021 회전하는 큐

import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
idx = list(map(int, sys.stdin.readline().rstrip().split()))

step = 0

def move_left(que):  # push back
    global step
    step += 1

    tmp = que.pop(0)
    que.append(tmp)


def move_right(que):  # push front
    global step
    step += 1

    tmp = [que.pop(-1)]
    tmp.extend(que)
    que = tmp

    return que

# que 만들기
que = list(range(1, n + 1))

# 원하는 수를 다 뽑을 때까지 반복
while idx:
    if que[0] == idx[0]:
        que.pop(0)
        idx.pop(0)
    else:
        # move left or right
        if que.index(idx[0]) <= len(que) // 2:
            while que[0] != idx[0]: move_left(que)
        else:
            while que[0] != idx[0]: que = move_right(que)
print(step)
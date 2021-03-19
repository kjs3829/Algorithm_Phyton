# BOJ 1697 숨바꼭질
# 그래프 탐색, 너비 우선 탐색
'''
bfs로 풀 수 있다면 dfs로도 풀 수 있다고 생각했었는데 그 것이 틀렸음을 알려준 문제.
문제에 맞는 탐색 기법이 있고, 그 것을 잘 찾아 내는 능력 또한 중요하다는 것을 깨달았다.
'''

import sys
from collections import deque
input = sys.stdin.readline


def bfs(n):
    queue = deque([[n, 0]])
    result = 0
    while queue:
        q = queue.popleft()
        visit[q[0]] = 1
        if q[0] == K:
            result = q[1]
            break
        if q[0] > 0 and visit[q[0]-1] == 0:
            queue.append([q[0]-1, q[1]+1])
        if q[0] + 1 <= 100000 and visit[q[0]+1] == 0:
            queue.append([q[0]+1, q[1]+1])
        if q[0] * 2 <= 100000 and visit[q[0]*2] == 0:
            queue.append([q[0]*2, q[1]+1])
    return result


N, K = map(int, input().split())
visit = [0]*100001
print(bfs(N))

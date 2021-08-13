# BOJ 1325 효율적인 해킹
# 그래프 탐색
import sys
from collections import deque
input = sys.stdin.readline


def bfs(start_node):
    visit = [0] * (N+1)
    q = deque()
    q.append(start_node)
    cnt = 0
    visit[start_node] = 1
    while q:
        p = q.popleft()
        cnt += 1
        for node in graph[p]:
            if not visit[node]:
                q.append(node)
                visit[node] = 1
    return cnt


N, M = map(int, input().split())    # 0 < N <= 10000, 0 < M <= 100000
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

max_trust, answer = 0, []
for i in range(1, N+1):
    if graph[i]:
        child_num = bfs(i)
        if child_num >= max_trust:
            if child_num > max_trust:
                answer.clear()
                max_trust = child_num
            answer.append(i)
print(*answer)

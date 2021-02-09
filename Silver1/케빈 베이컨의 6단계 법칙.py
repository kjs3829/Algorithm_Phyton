from sys import stdin
from collections import deque


def bfs(x):
    depth = [0]*(N+1)
    visit = [0]*(N+1)
    q = deque([x])
    visit[x] = 1
    while q:
        c = q.popleft()
        for i in range(len(graph[c])):
            if visit[graph[c][i]] == 0:
                q.append(graph[c][i])
                depth[graph[c][i]] = depth[c] + 1
                visit[graph[c][i]] = 1
    result = 0
    for x in depth:
        result += x
    return result


N, M = map(int, stdin.readline().split())
graph = [[] for x in range(N+1)]
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
min_sum = bfs(1)
r = 1
for i in range(2, N+1):
    if bfs(i) < min_sum:
        min_sum = bfs(i)
        r = i
print(r)


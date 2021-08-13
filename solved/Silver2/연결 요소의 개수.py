# BOJ 11724 연결 요소의 개수
# 그래프 이론
import sys
from collections import deque
input = sys.stdin.readline


def dfs(idx):
    stack = [graph[idx]]
    while stack:
        p = stack.pop()
        for i in range(len(p)):
            if visit[p[i]] == 0:
                stack.append(graph[p[i]])
                visit[p[i]] = 1


def bfs(idx):
    queue = deque([graph[idx]])
    while queue:
        p = queue.popleft()
        for i in range(len(p)):
            if visit[p[i]] == 0:
                queue.append(graph[p[i]])
                visit[p[i]] = 1


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visit = [0]*(N+1)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
cnt = 0
for i in range(1, N+1):
    if visit[i] == 0:
        cnt += 1
        bfs(i)
print(cnt)

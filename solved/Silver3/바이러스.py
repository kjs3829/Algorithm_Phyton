# BOJ 2606 바이러스
# 그래프 이론
from sys import stdin


def dfs(n):
    stack = [n]
    cnt = 0
    while stack:
        p = stack.pop()
        if visit[p] == 0:
            for i in range(len(graph[p])):
                stack.append(graph[p][i])
            visit[p] = 1
            cnt += 1
    return cnt


n = int(stdin.readline())
m = int(stdin.readline())
graph = [[] for _ in range(n+1)]
visit = [0]*(n+1)
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
print(dfs(1)-1)

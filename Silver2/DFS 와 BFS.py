# BOJ 1260 DFS와 BFS
# 그래프 이론
from sys import stdin
from sys import setrecursionlimit
from collections import deque
setrecursionlimit(10**6)
result_dfs = []
result_bfs = []


def dfs(n):
    if visit_dfs[n] == 0:
        result_dfs.append(str(n))
        visit_dfs[n] = -1
        for idx in range(len(way[n])):
            dfs(way[n][idx])


def bfs(n):
    move_to = deque([n])
    result = []
    while move_to:
        c = move_to.popleft()
        if visit_bfs[c] == 0:
            result.append(str(c))
            visit_bfs[c] = -1
            move_to += way[c]
    return result


N, M, V = map(int, stdin.readline().split())
way = [[] for _ in range(N+1)]
visit_dfs = [0]*(N+1)
visit_bfs = [0]*(N+1)
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    way[a].append(b)
    way[b].append(a)
for i in range(len(way)):
    way[i].sort()
dfs(V)
print(" ".join(result_dfs))
print(" ".join(bfs(V)))




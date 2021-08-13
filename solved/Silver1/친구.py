# BOJ 1058 친구
# 그래프 탐색
import sys
from collections import deque

input = sys.stdin.readline


def finding_two_friend_bfs(start_node):
    visit = [0]*N
    q = deque([start_node])
    visit[start_node] = 1
    while q:
        node = q.popleft()
        for child in graph[node]:
            if visit[child] == 0:
                q.append(child)
                visit[child] = visit[node] + 1
    cnt = -1
    for i in visit:
        if 0 < i <= 3:
            cnt += 1
    return cnt


N = int(input())
graph = [[] for _ in range(N)]
for parents_idx in range(N):
    info = input().rstrip()
    for child_idx in range(len(info)):
        if info[child_idx] == 'Y':
            graph[parents_idx].append(child_idx)

answer = 0
for person in range(N):
    answer = max(answer, finding_two_friend_bfs(person))
print(answer)

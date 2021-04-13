# BOJ 5014 스타트링크
# 너비 우선 탐색
# 시작 지점도 방문한 지점이라는 것을 간과해서 한번 틀린 문제
import sys
from collections import deque
input = sys.stdin.readline


def bfs(f,s,g,u,d):
    q = deque([s])
    visit[s] = 1
    while q:
        p = q.popleft()
        if p == g:
            return visit[p] - 1
        if p+u <= f and visit[p+u] == 0:
            q.append(p+u)
            visit[p+u] = visit[p] + 1
        if p-d > 0 and visit[p-d] == 0:
            q.append(p - d)
            visit[p - d] = visit[p] + 1
    return "use the stairs"


F, S, G, U, D = map(int, input().split())
visit = [0]*(F+1)
print(bfs(F,S,G,U,D))

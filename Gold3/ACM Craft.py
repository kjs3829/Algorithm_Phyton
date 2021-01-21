# Baekjoon 1005 ACM Craft
# 위상정렬 + dp

import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    D = [0] + list(map(int, sys.stdin.readline().split()))
    DP = [0] * (N + 1)
    inDegree = [0] * (N + 1)
    tree = [[] for _ in range(N+1)]
    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)
        inDegree[b] += 1

    order = deque()
    for i in range(1, N+1):
        if inDegree[i] == 0:
            order.append(i)
            DP[i] = D[i]

    while order:
        a = order.popleft()
        for i in tree[a]:
            inDegree[i] -= 1
            DP[i] = max(D[i]+DP[a], DP[i])
            if inDegree[i] == 0:
                order.append(i)
    W = int(sys.stdin.readline())
    print(DP[W])

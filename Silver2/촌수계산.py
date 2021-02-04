# BOJ 2644 촌수계산
# 자료구조, 트리
from sys import stdin

n = int(stdin.readline())
A = list(map(int, stdin.readline().split()))    # [a, b]
m = int(stdin.readline())
parent = [0]*(n+1)
for _ in range(m):
    x, y = map(int, stdin.readline().split())
    parent[y] = x
parent_a = [A[0]]
parent_b = [A[1]]
for c in range(2):
    p = parent[A[c]]
    while True:
        if p != 0:
            if c == 0:
                parent_a.append(p)
            else:
                parent_b.append(p)
            p = parent[p]
        else:
            break
exist, com = False, 0
for a in range(len(parent_a)):
    if exist:
        break
    for b in range(len(parent_b)):
        if parent_a[a] == parent_b[b]:
            com = parent_a[a]
            exist = True
            break
if exist:
    print(parent_a.index(com)+parent_b.index(com))
else:
    print(-1)


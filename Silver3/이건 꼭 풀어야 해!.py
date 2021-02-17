# BOJ 17390 이건 꼭 풀어야 해!
# 누적 합, 정렬
from sys import stdin
n, q = map(int, stdin.readline().split())
a = sorted(map(int, stdin.readline().split()))
for i in range(1, n):
    a[i] += a[i-1]
for _ in range(q):
    l, r = map(int, stdin.readline().split())
    print(a[r-1]) if l < 2 else print(a[r-1] - a[l-2])

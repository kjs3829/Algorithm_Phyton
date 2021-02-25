# BOJ 1182 부분수열의 합
# 브루트포스, 조합, dfs
from itertools import combinations
from sys import stdin

n, s = map(int, stdin.readline().split())
p = list(map(int, stdin.readline().split()))
cnt = 0
for i in range(1, n + 1):
    comb = list(map(sum, combinations(p, i)))
    cnt += comb.count(s)
print(cnt)

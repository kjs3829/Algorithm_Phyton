# BOJ 15663 N과 M (9)
import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
p = list(map(int, input().split()))
c = tuple()
r = sorted(list(set(permutations(p, m))))
for i in r:
    print(*i)

# BOJ 10974 모든 순열
import itertools
from sys import stdin

N = int(stdin.readline())
l = [x for x in range(1, N+1)]
nPr = list(itertools.permutations(l, N))
for i in nPr:
    print(*i)

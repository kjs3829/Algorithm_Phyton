# Baekjoon 1427 소트인사이드

import sys

N = int(sys.stdin.readline())
A = []
A = list(map(int, str(N)))
A.sort(reverse=True)
for n in A:
    print(n, end="")

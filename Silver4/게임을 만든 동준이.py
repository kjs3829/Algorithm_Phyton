# Baekjoon 2847 게임을 만든 동준이

import sys

N = int(sys.stdin.readline().rstrip())
l = [int(sys.stdin.readline()) for _ in range(N)]
result = 0
for i in range(N-1, 0, -1):
    if l[i] <= l[i-1]:
        result += (l[i-1]-l[i]+1)
        l[i-1] = l[i]-1
print(result)

# BOJ 1057 토너먼트
# 수학, 브루트포스
import sys

N, a, b = map(int, sys.stdin.readline().split())
l = max(a,b)
s = min(a,b)
result = 1
flag = True
while flag:
    max_round = 1
    while 2 ** max_round < N:
        max_round += 1
    if max_round == 1:
        break
    for r in range(max_round, 1, -1):
        std = 2 ** (r-1)
        if l <= std:
            N = std
        elif s <= std < l:
            result = r
            flag = False
            break
        else:
            s -= std
            l -= std
            N -= std
            break

print(result)

# BOJ 1205 등수 구하기
# 정렬
from sys import stdin

N, score, P = map(int, stdin.readline().split())
if N > 0:
    score_list = sorted(list(map(int, stdin.readline().split())) + [score], reverse=True)
    print(-1) if N == P and score <= score_list[-1] else print(score_list.index(score) + 1)
else:
    print(1)

# BOJ 1302 베스트셀러
# 자료구조, 정렬, 해시
from sys import stdin

N = int(stdin.readline())
d = dict()
for _ in range(N):
    t = stdin.readline().rstrip()
    if t in d:
        d[t] += 1
    else:
        d[t] = 1
print(sorted(d.items(), key=lambda x: (-x[1], x[0]))[0][0])

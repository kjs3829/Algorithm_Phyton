# BOJ 1476 날짜 계산
# 브루트포스
from sys import stdin

E, S, M = map(int, stdin.readline().split())
e, s, m = 0, 0, 0
cnt = 0
while E!=e or S!=s or M!=m:
    e += 1
    s += 1
    m += 1
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1
    cnt += 1
print(cnt)


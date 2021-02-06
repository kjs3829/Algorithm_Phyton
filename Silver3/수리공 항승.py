# BOJ 1449 수리공 항승
# 그리디
from sys import stdin

n, l = map(int, stdin.readline().split())
pl = list(map(int, stdin.readline().split()))
pl.sort()
cnt = 0
tmp = 0
for p in pl:
    if tmp < p:
        cnt += 1
        tmp = p + l - 1
print(cnt)

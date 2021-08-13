# BOJ 1436 영화감독 숌
# 브루트포스
import sys

N = int(sys.stdin.readline())
cnt = 0
i = 0
while cnt != N:
    if str(i).find("666") != -1:
        cnt += 1
    i += 1
print(i-1)

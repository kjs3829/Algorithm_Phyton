# BOJ 1931 회의실 배정
# 정렬
import sys
input = sys.stdin.readline

time = []
for i in range(int(input())):
    time.append(list(map(int, input().split())))
time.sort(key=lambda x: x[0])
time.sort(key=lambda x: x[1])
l, cnt = 0, 0
for i, j in time:
    if i >= l:
        cnt += 1
        last = j
print(cnt)

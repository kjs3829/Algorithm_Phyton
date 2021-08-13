# BOJ 2512 예산
# 이분 탐색
from sys import stdin

N = int(stdin.readline())
l = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
right = max(l)
left = 0
while left <= right:
    mid = (right+left)//2
    cnt = 0
    for i in l:
        if i >= mid:
            cnt += mid
        else:
            cnt += i
    if cnt <= M:
        left = mid + 1
    else:
        right = mid - 1
print(right)

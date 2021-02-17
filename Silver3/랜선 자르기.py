# BOJ 1654 랜선 자르기
# 이분 탐색
from sys import stdin

k, n = map(int, stdin.readline().split())
lans = [int(stdin.readline()) for _ in range(k)]
left, right = 1, max(lans)
while left <= right:
    mid = (right + left) // 2
    r = 0
    for i in range(len(lans)):
        r += lans[i]//mid
    if r >= n:
        left = mid + 1
        ans = mid
    else:
        right = mid - 1
print(ans)

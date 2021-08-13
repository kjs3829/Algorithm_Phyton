# BOJ 1940 주몽
# 브루트포스, 정렬
from sys import stdin
n = int(stdin.readline())
m = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
nums.sort()
cnt = 0
i, j = 0, n - 1
while i < j:
    if nums[i] + nums[j] == m:
        cnt += 1
        i += 1
        j -= 1
    elif nums[i] + nums[j] < m:
        i += 1
    else:
        j -= 1

print(cnt)

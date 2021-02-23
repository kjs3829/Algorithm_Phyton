# BOJ 1912 연속합
# DP
# 시간초과 실패, 다른 방법을 다시 생각해 봐야됨.

from sys import stdin
n = int(stdin.readline())
p = list(map(int, stdin.readline().split()))
result = p[0]
for i in range(1, len(p)):
    p[i] += p[i-1]
    if p[i] > result:
        result = p[i]

for r in range(len(p)):
    for c in range(r+1, len(p)):
        if p[c] - p[r] > result:
            result = p[c] - p[r]
print(result)

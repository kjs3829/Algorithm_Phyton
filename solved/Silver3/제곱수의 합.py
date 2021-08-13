# BOJ 1699 제곱수의 합
# DP
# min함수를 사용했더니 시간 초과가 뜸
# if문이 min함수보다 빠르다.
from sys import stdin
import math

N = int(stdin.readline())
dp = [0, 1, 2] + [100000]*99999
for i in range(3, N+1):
    r = int(math.sqrt(i))
    for j in range(r, 0, -1):
        if 1 + dp[i-j*j] < dp[i]:
            dp[i] = 1 + dp[i-j*j]
print(dp[N])

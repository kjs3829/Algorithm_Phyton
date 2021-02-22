# BOJ 1929 소수 구하기
# 에라토스테네스의 체
from sys import stdin
import math

l = [0, -1] + [0]*999999
M, N = map(int, stdin.readline().split())
for i in range(2, int(math.sqrt(1000000))):
    if l[i] == -1:
        continue
    j = 2
    while i * j <= 1000000:
        l[i*j] = -1
        j += 1
for i in range(M, N+1):
    if l[i] == 0:
        print(i)

# BOJ 1026 보물
# 정렬
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort(reverse=True)

r = 0
for i in range(N):
    r += A[i] * B[i]
print(r)

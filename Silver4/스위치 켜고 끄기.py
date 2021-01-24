# Baekjoon 2217 로프

import sys

N = int(sys.stdin.readline())
rope = []
value = []
for i in range(N):
    rope.append(int(sys.stdin.readline()))
rope.sort(reverse=True)
for num in range(N):
    value.append(rope[num]*(num+1))
print(max(value))

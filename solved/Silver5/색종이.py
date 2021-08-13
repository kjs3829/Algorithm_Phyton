# BOJ 2563 색종이
# 구현
from sys import stdin
N = int(stdin.readline())
paper = [[0]*101 for _ in range(101)]
area = 0
for i in range(N):
    x,y = map(int,input().split())
    for j in range(x,x+10):
        for k in range(y,y+10):
            paper[j][k] = 1

for r in paper:
    if 1 in r:
        area += sum(r)
print(area)

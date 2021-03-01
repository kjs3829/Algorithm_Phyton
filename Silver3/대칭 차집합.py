# BOJ 1269 대칭 차집합
import sys
input = sys.stdin.readline

x, y = map(int, input().split())
a = dict(zip(list(map(int, input().split())), [0]*x))
b = dict(zip(list(map(int, input().split())), [0]*y))

cnt = 0
for i in b:
    if a.setdefault(i, -1) == -1:
        cnt += 1
for i in a:
    if b.setdefault(i, -1) == -1:
        cnt += 1
print(cnt)







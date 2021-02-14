# BOJ 11656 접미사 배열
from sys import stdin

s = list(stdin.readline().rstrip())
a = []
while s:
    a.append(''.join(s))
    s.pop(0)
for i in sorted(a):
    print(i)

# BOJ 17219 비밀번호 찾기

from sys import stdin

N, M = map(int, stdin.readline().split())
add = {}

for _ in range(N):
    site, ps = stdin.readline().split()
    add[site] = ps

for _ in range(M):
    print(add[stdin.readline().rstrip()])

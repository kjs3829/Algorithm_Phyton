# BOJ 14425 문자열 집합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a, cnt = {}, 0
for _ in range(n):
    a[input().rstrip()] = 1
for _ in range(m):
    if a.get(input().rstrip()):
        cnt += 1
print(cnt)

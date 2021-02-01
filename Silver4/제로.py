# BOJ 10773 제로
from sys import stdin

n = int(stdin.readline())
z = []
for i in range(n):
    num = int(input())
    if num == 0:
        z.pop()
    else:
        z.append(num)
print(sum(z))

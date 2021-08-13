# BOJ 13305 주유소
from sys import stdin
from sys import maxsize

N = int(stdin.readline())
road = list(map(int, stdin.readline().split()))
price = list(map(int, stdin.readline().split()))
total = 0
minV = maxsize

for i in range(N - 1):
    if i == 0:
        total += price[0] * road[0]
        minV = min(minV, price[i])
    else:
        minV = min(minV, price[i])
        total += minV * road[i]
print(total)

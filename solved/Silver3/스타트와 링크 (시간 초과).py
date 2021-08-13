# BOJ 14889 스타트와 링크
# 시간 초과뜸
from itertools import combinations
from itertools import permutations
from sys import stdin
from copy import deepcopy


def overall(lst):
    test2 = list(permutations(lst, 2))
    sum = 0
    for i in test2:
        sum += mat[i[0]][i[1]]
    return sum


n = int(stdin.readline())
mat = [[0]*(n+1)] + [[0] + list(map(int, stdin.readline().split())) for _ in range(n)]
p = [i for i in range(1, n+1)]
total_sum, diff = 0, 100000000
for i in range(1, n+1):
    total_sum += sum(mat[i])

for i in range(2, n//2+2):
    start_team = list(combinations(p, i))
    for j in range(len(start_team)):
        link_team = deepcopy(p)
        for c in start_team[j]:
            link_team.remove(c)
        diff = min(abs(overall(start_team[j])-overall(link_team)), diff)
print(diff)

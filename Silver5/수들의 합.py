# Baekjoon 1789 수들의 합

import sys

N = int(sys.stdin.readline())

temp = 1
answer = 0

while True:
    N -= temp

    if N >= 0:
        answer += 1
        temp += 1

    else:
        print(answer)
        break
